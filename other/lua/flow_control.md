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



# Flow control

This section describes the flow control operatora available in lua.

## If

The `if` syntax is really intuitive. The only thing to know is that it interprets
only `false` boolean and `nil` as false statements. The numbers
**0 and negatives are interpreted as a positived statement**.

---

The short code snipped that describes the idea:


```lua
if nil then
    print("no execution")
elseif 0 then
    print("it will be executed")
end
```

<!-- md-runner-output:start -->
```text
it will be executed

```
<!-- md-runner-output:end -->

## Cycles

Lua supports 4 types of cycles:

- Two subtupes of for look:
  - Numerical: `for Name ‘=’ exp ‘,’ exp [‘,’ exp] do block end`. Iterates over
    a set range of numbers.
  - Generic: `for namelist in explist do block end`. Iterates over functions,
    called iterators.
- `while exp do block end`.
- `repeat block until exp`. Repeats the `block` until `exp` is correct.

### For

There are two classical loops in lua: `for` and `while`.

---

The following cell provides an option to define a for loop that iterates over the
index:


```lua
for index=1, 5 do
    print(index)
end
```

<!-- md-runner-output:start -->
```text
1
2
3
4
5

```
<!-- md-runner-output:end -->

There is another option for the `for` loop. The syntax  
`for <variables> in <iterator triplet>` could be used. The returns the objects
at each iteration, which would be assiged to the `variables`.

The following cell demonstrates this kind of syntax using the `ipairs` function,
which returns the iterator triplet that iterates over the sequence stored in the
table:


```lua
for index, val in ipairs({20, 30, 2, 1, key=value}) do
    print(index, val)
end
```

<!-- md-runner-output:start -->
```text
1	20
2	30
3	2
4	1

```
<!-- md-runner-output:end -->

The syntax of the while loop is really straight:


```lua
i = 1
while i < 5 do
    print(i)
    i = i + 1
end
```

<!-- md-runner-output:start -->
```text
1
2
3
4

```
<!-- md-runner-output:end -->
