<!-- md-runner
{
  "executors": {
    "lua": {
      "module": "md_runner.executors.lua",
      "params": {
        "lua": "lua"
      }
    },
    "bash": {
      "module": "md_runner.executors.bash"
    }
  }
}
-->

# Lua

Lua is an interpreted programming language that is popular to be language for
creating plugins for different software.

This notebook uses [xeus-lua](https://github.com/jupyter-xeus/xeus-lua) kernel to show the aspects of lua.

## Functions

The functions in lua are really intuitive. However, there are some important
details to be aware of. Check the [Functions](lua/functions.ipynb) page.

---

There are two syntaxes for defining a function, both of which are represented in
the following example:

```lua
function hello(name)
    print("Hello!", name)
end

hello("Lua")
```

<!-- md-runner-output:start -->
```text
Hello!	Lua

```
<!-- md-runner-output:end -->



```lua
hello2 = function(name)
    print("Hello!", name)
end

hello2("Lua2")
```

<!-- md-runner-output:start -->
```text
Hello!	Lua2

```
<!-- md-runner-output:end -->

## Tables

Lua offers the `table` datatype to store data. This object can represent both
sequences and mappings.

Check more details in the specific [tables](lua/tables.ipynb) page.

---

The following cell defines the `table1` as table:

```lua
tab = {
    'the first element',
    key1 = 'value1',
    ['key2'] = 'value2'
}
print(tab)

for key, value in pairs(tab) do
    print(key, value)
end
```

<!-- md-runner-output:start -->
```text
table: 0x5715b54489f0
1	the first element
key1	value1
key2	value2

```
<!-- md-runner-output:end -->

Here are table that contains:

- The "the first element" string as the first element of the sequence. 
- Under the `key1` hides value `value1`.
- Under the `key2` hides value `value2`.

By accessing the first index of the table, you retrieve value that is defined as
an element of the table:

```lua
print(tab[1])
```

<!-- md-runner-output:start -->
```text
the first element

```
<!-- md-runner-output:end -->

There are different ways to access the values under the mapping:

```lua
print(tab['key1'], tab['key2'])
```

<!-- md-runner-output:start -->
```text
value1	value2

```
<!-- md-runner-output:end -->

```lua
print(tab.key2)
```

<!-- md-runner-output:start -->
```text
value2

```
<!-- md-runner-output:end -->

### Iterating

To iterate through tables, there are two functions that transform a table into interator:

- `pairs`: iterates over all elements of table.
- `ipairs`: interates only over list elements of the table.

---

The following cell creates the `some_table` that will be used to demonstrate the
ways to iterate over table.

```lua
some_table = {
    key1 = "value1",
    key2 = "value2",
    "obj1",
    "obj2",
    "obj3"
}
```

The output of `pairs` contains both list-based and key-value elements of the table:

```lua
for key, value in pairs(some_table) do
    print(key, value)
end
```

<!-- md-runner-output:start -->
```text
1	obj1
2	obj2
3	obj3
key2	value2
key1	value1

```
<!-- md-runner-output:end -->

The `ipairs` output contains only list-based values:

```lua
for key, value in ipairs(some_table) do
    print(key, value)
end
```

<!-- md-runner-output:start -->
```text
1	obj1
2	obj2
3	obj3

```
<!-- md-runner-output:end -->

## Flow control

The flow control constructions available in lua are listed in the following table:

| Construct                                          | Description                                     |
| -------------------------------------------------- | ----------------------------------------------- |
| `if ... then ... end`                              | Conditional execution.                          |
| `if ... then ... else ... end`                     | Conditional execution with alternative branch.  |
| `if ... then ... elseif ... then ... else ... end` | Multi-branch conditional.                       |
| `while ... do ... end`                             | Pre-condition loop.                             |
| `repeat ... until`                                 | Post-condition loop (runs at least once).       |
| `for i = start, stop [, step] do ... end`          | Numeric loop.                                   |
| `for ... in ... do ... end`                        | Generic loop using iterators.                   |
| `break`                                            | Exits the innermost loop.                       |
| `goto label`                                       | Jumps to a label within the same function.      |
| `::label::`                                        | Defines a label for `goto`.                     |
| `return`                                           | Exits a function and optionally returns values. |
| `do ... end`                                       | Creates a local scope block.                    |

Check mode detailed explanation with some examples in the dedicated
[Flow control](lua/flow_control.ipynb) page.

## String

Here is a of the most basic things about the basic string dtype in lua:

- **Creation** - Strings can be created with single quotes (`'...'`), double
  quotes (`"..."`), or long bracket syntax (`[[...]]`) for multiline text.
- **Immutable** - Strings cannot be modified in place; any operation that changes
  a string returns a new one.
- **Concatenation** - Use the `..` operator to join strings together.
- **Length** - The `#` operator returns the string length in **bytes**, not
  Unicode characters.
- **String library** - Most operations are provided by the `string` library
  (`sub`, `find`, `match`, `gsub`, `format`, etc.).

Check section [6.5 - String Manipulation](https://www.lua.org/manual/5.5/manual.html#6.5)
for description of features and standard library functions.

---

The following cell writes to the `multiline` multiline string literal. It also
shows the length of the given string variable:


```lua
multiline = [[
The text
to check
]]
print(#multiline)
```

<!-- md-runner-output:start -->
```text
18

```
<!-- md-runner-output:end -->

### Patterns

There is a special language for defining string patterns. It looks similar to
regular expression syntax, but actually simpler and supports a smaller feature set.

For more check the [6.5.1 - Patterns](https://www.lua.org/manual/5.5/manual.html#6.5.1) section of the documentation.

```lua
str = [[
    indent1
        indent2
    indent1
        imdent2
]]

indent = str:match("[ \t]+")
print(#indent)
```

<!-- md-runner-output:start -->
```text
4

```
<!-- md-runner-output:end -->



```lua
indent = str:match("\n([ \t]+)")
print(#indent)
```

<!-- md-runner-output:start -->
```text
8

```
<!-- md-runner-output:end -->

## Standard library

Check the [Standard libraries](https://www.lua.org/manual/5.5/manual.html#6) reference page.

The following talbe show the most essential functions of the lua standard library:

| Name       | Description                                                                             |
| ---------- | --------------------------------------------------------------------------------------- |
| `print`    | Prints values to standard output, converting them to strings.                           |
| `type`     | Returns the type of a value (`"nil"`, `"number"`, `"string"`, `"table"`, etc.).         |
| `pairs`    | Returns an iterator for traversing all key-value pairs in a table.                      |
| `ipairs`   | Returns an iterator for traversing the integer-indexed elements of an array-like table. |
| `next`     | Returns the next key-value pair in a table; used internally by `pairs`.                 |
| `tonumber` | Converts a value to a number if possible.                                               |
| `tostring` | Converts a value to its string representation.                                          |
| `pcall`    | Calls a function in protected mode, catching errors instead of raising them.            |
| `require`  | Loads and returns a module, caching it for future use.                                  |
| `error`    | Raises an error and stops normal execution unless caught by `pcall` or `xpcall`.        |

## Modules

The important builtin facilities to manupulate with modules:

- The `package` table contains the attributes that determine module-related behaviour.
- The `require` function loads the module.
- The `dofile` function imedately executes the given file.

The module is simply a lua file that returns a value. Typically, this is table
named `M` that contains references to all the objects the module provides.

Check more in the [Modules](https://www.lua.org/manual/5.5/manual.html#6.4) section of the lua manual.

---

Consider the module `lua_files/example.lua`:

```lua
M = {}

M.some_function = function()
    print("This is function from module")
end

return M
```

The code that imports that module:


```lua
example_module = require("other.lua_files.example")

print(example_module)
print(example_module['some_function'])
```

<!-- md-runner-output:start -->
```text
table: 0x563464bc2a20
function: 0x563464bbb490

```
<!-- md-runner-output:end -->

The usage of `some_function` has the expected behaviour:

```lua
example_module.some_function()
```

<!-- md-runner-output:start -->
```text
This is function from module

```
<!-- md-runner-output:end -->

Now consider the `package` table:

```lua
print(type(package))
```

<!-- md-runner-output:start -->
```text
table

```
<!-- md-runner-output:end -->

As key-values it contains all the modules that have been loaded into the environment:

```lua
for k, _ in pairs(package.loaded) do
    print(k)
end
```

<!-- md-runner-output:start -->
```text
package
os
string
_G
other.lua_files.example
math
coroutine
utf8
debug
table
io

```
<!-- md-runner-output:end -->

For example, the file `lua_files.example` that was imported manually. The
following cell accesses the module through `package.loaded` table:

```lua
for key, value in pairs(package.loaded["other.lua_files.example"]) do
print(key, value)
end
```

<!-- md-runner-output:start -->
```text
some_function	function: 0x563464bbb490

```
<!-- md-runner-output:end -->

The `searchers` attribute of the `package` contains a set of functions that an
be used to search for modules. Consequently, you can implement your own
module-looking strategy simply by adding a new functions to this table:

```lua
for key, value in pairs(package.searchers) do
    print(key, value)
end
```

<!-- md-runner-output:start -->
```text
1	function: 0x563464bb5910
2	function: 0x563464bb5950
3	function: 0x563464bb5990
4	function: 0x563464bb59d0

```
<!-- md-runner-output:end -->

## Interpreter

The important features of the lua interpreter are:

- The `-i` allows to enter the interactive mode after running a given script.
- The `-l` parces and executes the given library.
- The `-e` executes code passed through CLI.

---

```bash
lua -e 'print("hello from lua")'
```

<!-- md-runner-output:start -->
```text
hello from lua
```
<!-- md-runner-output:end -->
