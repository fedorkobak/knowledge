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
    },
    "text": {
      "module": "md_runner.executors.file"
    }
  }
}
-->
# Strings

This section considers the ways to work with string information in Lua.

## Format

The `string.format` function allows to substitute to string values with a set of
formatting option inspired from the `printf` C function.

The function takes `formatstring` as the first argument. This should be a template
with special 'specifiers', which the function is supposed to substitute.
These specifiers contain the information how the substitution should be performed.

All following arguments specifies the values to be formated and substituted.

---

This simple example sets the `formatstring`, which contains a specifier for a
string, quoted string and a hexadecimal number.

The call of the `string.format` specifies the values to be substituted.

```lua
formatstring = 'the value %s, %q, %x'
print(string.format(formatstring, 'just string', 'quoted one', 10))
```

<!-- md-runner-output:start -->
```text
the value just string, "quoted one", a

```
<!-- md-runner-output:end -->

The result is that the placeholders in the formatting string now have
corresponding values with the same formatting.

### Specifiers

The list of possible specifiers:

| Specifier | Description                         | Example                              | Output         |
|-----------|-------------------------------------|--------------------------------------|----------------|
| `%s`      | String                              | `string.format("%s", "hello")`       | `hello`        |
| `%d`      | Signed decimal integer              | `string.format("%d", 42)`            | `42`           |
| `%i`      | Signed decimal integer              | `string.format("%i", 42)`            | `42`           |
| `%f`      | Floating-point number               | `string.format("%f", 3.14)`          | `3.140000`     |
| `%e`      | Scientific notation                 | `string.format("%e", 1234.5)`        | `1.234500e+03` |
| `%E`      | Scientific notation (uppercase)     | `string.format("%E", 1234.5)`        | `1.234500E+03` |
| `%g`      | Shorter of `%f` and `%e`            | `string.format("%g", 3.14)`          | `3.14`         |
| `%G`      | Like `%g`, uppercase exponent       | `string.format("%G", 3.14)`          | `3.14`         |
| `%x`      | Hexadecimal integer                 | `string.format("%x", 255)`           | `ff`           |
| `%X`      | Uppercase hexadecimal               | `string.format("%X", 255)`           | `FF`           |
| `%o`      | Octal integer                       | `string.format("%o", 8)`             | `10`           |
| `%u`      | Unsigned decimal integer            | `string.format("%u", 42)`            | `42`           |
| `%c`      | Character from integer code         | `string.format("%c", 65)`            | `A`            |
| `%q`      | Quoted, Lua-readable representation | `string.format("%q", "hello")`       | `"hello"`      |
| `%a`      | Hexadecimal floating-point          | `string.format("%a", 1.5)`           | `0x1.8p+0`     |
| `%%`      | Literal percent sign                | `string.format("100%%")`             | `100%`         |

## Patterns

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

## Substrings and indexing

The typical `[]` operator doesn't work for Lua strings. The unified method is to
use the `string.sub` function or the method `sub` of the string.

---

The following code shows the usage of the `string.sub` function:

```lua
value = 'the string'

print(string.sub(value, 1, 5))
```

<!-- md-runner-output:start -->
```text
the s

```
<!-- md-runner-output:end -->

It's usually more practical to use the `:sub` method of the string. For example
iterating over the symbols of the string:

```lua
value = 'the symbols'

for i = 1, #value do
    print(value:sub(i, i))
end
```

<!-- md-runner-output:start -->
```text
t
h
e
 
s
y
m
b
o
l
s

```
<!-- md-runner-output:end -->

## Unicode

One of the most significant details of the implmentatioin of strings in Lua is
that they are considered as sequences of bytes; there is no builtin abstraction
for the symbol.

Some Unicode symbols are composed of several bytes, so there are a lof of issues
associated with managing strings containing Unicode symbols in Lua.

---

As the example consider the following string that contains russian symbols that
are not covered with ACII table:

```lua
val = 'Привет'
print(#val)
```

<!-- md-runner-output:start -->
```text
12

```
<!-- md-runner-output:end -->

The string is twice as long because all symbols are conpose of two bytes.
However, Lua does not recognise the difference between them.

Consider tactual codes of the bytes that make up this string:

```lua
for i = 1, #val do
    io.write(string.format('%x', val:byte(i)), ' ')
end
```

<!-- md-runner-output:start -->
```text
d0 9f d1 80 d0 b8 d0 b2 d0 b5 d1 82 
```
<!-- md-runner-output:end -->
