<!-- md-runner
{
  "executors": {
    "lua": {
      "module": "md_runner.executors.lua",
      "params": {
        "lua": "lua"
      }
    }
  }
}
-->
# Tables

The table is the only datastructure available in lua. You are supposed to use
it to build all kind of abstractions, from sequences to inherited classes.

## Sequences

The set of elements with positive integer indices from 1 to given n without holes
is called - sequence. In lua sequences have a lot of usefull properties which
are considered in this section.

- `table.insert`: to add the element.
- `table.remove`: to remove the element.
- `#<table_name>`: to get the length of list elements in table.
- `iparis`: function iterates only over list elements

Check more in the [corresponding page](tables/sequences.md).

## Methods

There is no such thing as a 'method' in lua. However, you can store functions in
the tables and pass the table itself to them as an argument.

Lua has a special operator for this: column `:`:

**Define the method** using syntax:

```lua
function table_name:method_name(param1, param2, param3)
...
end
```

The key feature of the method is that it automatically defines the `self`
parameter, which you can use in the function body.

In Lua's logic, it is formally still a function with an implicitly defined `self`
parameter. Therefore, if you call in the usual way using the `.` operator, you
must implicitly an argument for `self`. To simplify that `:` can be used to
assign to the method of the table:

```lua
val = table_name:method_name(arg1, arg2, arg3)
```

---

The following cell shows the table that has:

- `column_method` defined through `:` operator.
- `regular_functions` defined through `.` operator.

Both of them are trying to print the `self` object.

```lua
some_table = { value = 'the value' }

function some_table:column_method()
    if self then
        for i, v in pairs(self) do print(i, v) end
    else
        print('the self is nil')
    end
end

function some_table.regular_function()
    if self then
        for i, v in pairs(self) do print(i, v) end
    else
        print('the self is nil')
    end
end
```

First, assign to the `column_method` through `:`:

```lua
some_table:column_method()
```

<!-- md-runner-output:start -->
```text
column_method	function: 0x629463689d60
value	the value
regular_function	function: 0x629463681040

```
<!-- md-runner-output:end -->

This is the regular behaviour of the method. The `self` simply refers to the
`some_table` itself.

However, the same result could be achieved explicitly:

```lua
some_table.column_method(some_table)
```

<!-- md-runner-output:start -->
```text
column_method	function: 0x629463689d60
value	the value
regular_function	function: 0x629463681040

```
<!-- md-runner-output:end -->

And an attempt to call the `regular_function` through the `:` operator:

```lua
some_table:regular_function()
```

<!-- md-runner-output:start -->
```text
the self is nil

```
<!-- md-runner-output:end -->

Even though the function was called with the `:` operator, the `self` argument
cannot be accessed in the function body as it was not defined.

## Meta tables

Metatables allow you to define how a table behaves in specific cases.

You can define a special table where defined the methods with special names
which determine the behaviour of the tableale. The basic special methods:

| Metamethod   | Triggered by                         |
| ------------ | ------------------------------------ |
| `__index`    | `t[key]` when key is missing         |
| `__newindex` | `t[key] = value` when key is missing |
| `__add`      | `a + b`                              |
| `__sub`      | `a - b`                              |
| `__mul`      | `a * b`                              |
| `__div`      | `a / b`                              |
| `__mod`      | `a % b`                              |
| `__pow`      | `a ^ b`                              |
| `__unm`      | `-a`                                 |
| `__concat`   | `a .. b`                             |
| `__len`      | `#a`                                 |
| `__eq`       | `a == b`                             |
| `__lt`       | `a < b`                              |
| `__le`       | `a <= b`                             |
| `__call`     | `a(...)`                             |
| `__tostring` | `tostring(a)`                        |
| `__pairs`    | `pairs(a)`                           |
| `__ipairs`   | `ipairs(a)` (Lua 5.2 only)           |

Use the `setmetatable(<arbitray_table>, <metatable>)` function to inherit the
special methods from the `metatable` to the `arbitrary_table`.

---

The following cell defines the `mt` metatable, which redfines the table's
indexing logic.

```lua
mt = {}

function mt:__index(i)
    if i <= #self and i > 0 then
        return self[i]
    else
        return 'no such element'
    end
end
```

Setting the `mt` as metatable for the new `table1`.

```lua
table1 = setmetatable({ 10, 20, 30 }, mt)
print(table1[1])
print(table1[40])
```

<!-- md-runner-output:start -->
```text
10
no such element

```
<!-- md-runner-output:end -->

As the result `table1` indexing logic behaves like specified in the `mt`.
