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

# Modules

This section considers how the files containing lua code can be incorporated
into the program.

## dofile

The `require` function loads the module, which involves more than just execution.
In contrast, the `dofile` function simply executes the specified file.

---

Consider file:

```lua
print("this is simple lua script")
for i = 1, 5 do
   print("conut " .. i)
end
```

And it's import with `dofile` function:

```lua
dofile("other/lua_files/dofile_example.lua")
```

<!-- md-runner-output:start -->
```text
this is simple lua script
conut 1
conut 2
conut 3
conut 4
conut 5

```
<!-- md-runner-output:end -->

**Note** that dofile requires a path that corresponds to the rules of the
operating system's rules not dot-separated path typical for lua.

## Searchpath

The `packages.searchpath(name, path [, sep [, rep]])` function searches for a
specified files.

The `name` determines the names of the file.

The `path` determines set of patterns where `name` would be substituted separted
by the `;`.

The first case in which the value of the `name` is substitued into the value of
the variable path, resulting in a path to an existing file that can be ingested,
returns the path to this file.

---

The following cell roughly shows how lua searches for the `.lua` files.

```lua
print(package.searchpath('example', './other/lua_files/?.lua'))
```

<!-- md-runner-output:start -->
```text
./other/lua_files/example.lua

```
<!-- md-runner-output:end -->

If the name or pattern are incorrect, the `nil` value and a message describing
the issue are returned.

```lua
print(package.searchpath('some_other', 'other/lua_files/?.lua'))
print(package.searchpath('example', 'other/lua_files/?'))
```

<!-- md-runner-output:start -->
```text
nil	no file 'other/lua_files/some_other.lua'
nil	no file 'other/lua_files/example'

```
<!-- md-runner-output:end -->
