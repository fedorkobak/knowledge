# Strings

This section considers the ways to work with string information in Lua.

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

