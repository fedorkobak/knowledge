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
# Sequences

A sequence is a set of elements with consecutive integer indices. Sequences are
typical way to implement a lot of functionality. This page considers the
properties of sequences.

## Insert/remove

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


## Holes

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
