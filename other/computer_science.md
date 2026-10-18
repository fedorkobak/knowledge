<!-- md-runner
{
  "executors": {
    "bash": {
      "module": "md_runner.executors.bash"
    },
    "python": {
        "module": "md_runner.executors.python"
    }
  }
}
-->
# Computer science

This page covers the topics of general computer science topics, independent of
any specific tool.

## Numbers represenation

A computer is a machine that can perform operations on number. However, these
numbers are represented in **binary format**.

Also, a popular way of representing a number is in **hexadecimal** - numering system
were there are 16 different digits.

Another important concept is the principle of storing floating-point numbers in
computers. This involves adapting scientific notation to a binary representation.

### Binary

In binary format, any number is represented using only digits 0 and 1.
The widely used notation for binary numbres is `0b<number>`, most programming
languages and specific use this notation.

---

The following code demonstrates python facilities to convert the number 16 to
the binary format and support of the corresponding notation.

```python
print(bin(16))
print(0b1010)
```

<!-- md-runner-output:start -->
```text
0b10000
10

```
<!-- md-runner-output:end -->

## Unicode

UTF-8 is the most popular method for representing text on computer.
UTF-8 encoding is usually written as `U+uvwxyz`, where `uvwxyz` is 6-digit hex number.

Depending on how far the symbol if from the beginning of the table, it can take
from one to four bytes.

Check the [Common References for Unicode Standard](https://unicode.org/reports/tr41/tr41-36.html).
It contains various technical details about the Unicode specification. This sidte
considers the features of the latest unicode standard if other is not mentioned
specifically.

Sometimes it can be usefull to find the specific character and data related to
it. Check the [Unicode Character Database](https://www.unicode.org/ucd/).

---

The `uniname` utility in the `uniutils` package displays information about the
encoding of a given string in table form. The following cell shows the output
for a few of the first Latin symbols.


```bash
export LINES=100
echo "abcde" | uniname -A
```

<!-- md-runner-output:start -->
```text
character  byte       UTF-32   encoded as     glyph   name
        0          0  000061   61             a      LATIN SMALL LETTER A
        1          1  000062   62             b      LATIN SMALL LETTER B
        2          2  000063   63             c      LATIN SMALL LETTER C
        3          3  000064   64             d      LATIN SMALL LETTER D
        4          4  000065   65             e      LATIN SMALL LETTER E

```
<!-- md-runner-output:end -->

The following cell shows the outputs of the `uniname` for some cirilic letters.


```bash
echo "абвгд" | uniname -A
```

<!-- md-runner-output:start -->
```text
character  byte       UTF-32   encoded as     glyph   name
        0          0  000430   D0 B0          а      CYRILLIC SMALL LETTER A
        1          2  000431   D0 B1          б      CYRILLIC SMALL LETTER BE
        2          4  000432   D0 B2          в      CYRILLIC SMALL LETTER VE
        3          6  000433   D0 B3          г      CYRILLIC SMALL LETTER GHE
        4          8  000434   D0 B4          д      CYRILLIC SMALL LETTER DE

```
<!-- md-runner-output:end -->

To check which character that corresponds to a specific unicode point, you can use the `pringf` bash command with the `\U` modifier.


```bash
printf "\u0061"
printf "\U007A"

printf "\U0001F600"
```

<!-- md-runner-output:start -->
```text
az😀
```
<!-- md-runner-output:end -->

### Layers of character

There are three layers that defines each character in unicode:

- **Abstract character**: the single piece of information. The concept itself.
- **Code point**: the numerical value assigned to that concept.
- **Glyph**: the spefic "image" that represents the code point. Each font have
  it's own glyphes.

---

For example, consider the case where to the same abstract character "latin small
letter e with acute" has two representations:

```bash
printf "\u00E9"
printf "\u0065\u0301"
```

<!-- md-runner-output:start -->
```text
éé
```
<!-- md-runner-output:end -->

First uses just code point `U+00E9`, second is composed from `U+0065` and
`U+0301`, but the abstract character is the same.

The following example illustrates the case in which two code point have the same
abstract character due to compatibilities issues:

```bash
printf "\u212B"
printf "\u00C5"
```

<!-- md-runner-output:start -->
```text
ÅÅ
```
<!-- md-runner-output:end -->

### Normalization forms

The same human-readable text can be represented in Unicode in variety of ways.
There are normal forms of Unicode text that define a single way for text to be represented.

Check more in the [Unicode normalization forms](https://unicode.org/reports/tr15/).

---

The following cell shows how the same symbols that can be encoded differently in
Unicode.

```bash
printf "\u00C7"
printf "\u0043\U0327"
```

<!-- md-runner-output:start -->
```text
ÇÇ
```
<!-- md-runner-output:end -->
