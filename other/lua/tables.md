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

## Length

To get the length of the lua table use `#` operator.

**Note** it only counts sequential elements of the table; it ignores mappings.

---

The following cell defines a table containing two sequential elements and one
mapping pair:

```lua
length_table = {
    'value1', 'value2',
    ['map_key1'] = 'map value1'
}

print(#length_table)
```

<!-- md-runner-output:start -->
```text
2

```
<!-- md-runner-output:end -->

## List elements

Consider the typical operations associated with list elements of the table.

- `table.insert`: to add the element.
  - `table.insert(tab, value)` inserts the `value` as last elment.
  - `table.insert(tab, ind, value)` inserts value in `ind` position and shifts
    all others.
- `table.remove`: to remove the element.
  - `table.remove(tab)` removes the last list element.
  - `rable.remove(tab, ind)` removes the element with index `ind`.

These functions save the order of the elements

---

The following example crates creates the empty table and inserts to it some
values through `table.insert`:

```lua
tab = {}

table.insert(tab, 'hello')
table.insert(tab, 'last')
table.insert(tab, 1, 'first')

for k, v in ipairs(tab) do print(k, v) end
```

<!-- md-runner-output:start -->
```text
1	first
2	hello
3	last

```
<!-- md-runner-output:end -->

**Note** that the `first` element inserted in the position `1` and shifts all
the other elements.

The following code removes the value in the second position.

```lua
table.remove(tab, 2)
for k, v in pairs(tab) do print(k, v) end
```

<!-- md-runner-output:start -->
```text
1	first
2	last

```
<!-- md-runner-output:end -->

Using the `table.remove` without specifying of the position removes the last element:

```lua
table.remove(tab)
for k, v in ipairs(tab) do print(k, v) end
```

<!-- md-runner-output:start -->
```text
1	first

```
<!-- md-runner-output:end -->

### Holes

If some of the list elements do not follow the sequence, omit them from the end
\- such situation is called hole elements (or spared table).

These elements are not considered as list elements in the table until the
missing elemnts are completed. As the result, function that are suposed to rely
on sequence behave differently with such elements.

---

The following code creates a table with a 3-rd hole-element.

```lua
tab = {'first', 'second', [4] = 'fourth'}
```

The behaviour of the `#` operator and `iparis` function ignoes 4-th element.

```lua
print('length', #tab)
print()
for k, v in ipairs(tab) do print(k, v) end
```

<!-- md-runner-output:start -->
```text
length	2

1	first
2	second

```
<!-- md-runner-output:end -->

The `table.insert` inserts the element in the 3-rd position without shifting the
fourth.

```lua
table.insert(tab, 'third')
for k, v in ipairs(tab) do print(k, v) end
```

<!-- md-runner-output:start -->
```text
1	first
2	second
3	third
4	fourth

```
<!-- md-runner-output:end -->

Note that the last `ipairs` call included the 4-th element, which now is
considered as the element of the list:

```lua
table.insert(tab, 'fifth')
for k, v in ipairs(tab) do print(k, v) end
```

<!-- md-runner-output:start -->
```text
1	first
2	second
3	third
4	fourth
5	fifth

```
<!-- md-runner-output:end -->

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
