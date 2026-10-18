<!-- md-runner
{
  "executors": {
    "python": {
        "module": "md_runner.executors.python"
    }
  }
}
-->
# Numbers represenation

This page considers how numbers are represented in computer.

## Binary

In binary format, any number is represented using only digits 0 and 1.
The widely used notation for binary numbres is `0b<number>`, most programming
languages and specific use this notation.

The digits in a number represented in binary format have a special name: 'bits'.

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

The next code shows a group of integers converted into binary format.

```python
for i in range(10):
    print(i, bin(i))
```

<!-- md-runner-output:start -->
```text
0 0b0
1 0b1
2 0b10
3 0b11
4 0b100
5 0b101
6 0b110
7 0b111
8 0b1000
9 0b1001

```
<!-- md-runner-output:end -->

## Hexadecimal

Another popular way of representing number in computer science is hexadecimal.

In hexadecimal represenation each digit can take 16 values
$\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F\}$.

The decimal number 10 written in hexadecimal format is A, as it follows 9.

It is usefull as it allows relatively short representations of numbers while
maintaining a **digits correspondance** with the binary representation. Each
four digits of the binary have one-to-one correspondance with one digit in hexadecimal.

The standard notation for a hexadecimal is `0x<hexadecimal>`.

---

The following code shows the conversion `0xFDC` to the binary:

```python
print(bin(0xFDC))
```

<!-- md-runner-output:start -->
```text
0b111111011100

```
<!-- md-runner-output:end -->

In this example, the digit correspondence means:

```text
1111 1110 1100
  F    E    D
```

## Floating point

This involves representing each number as a main part, which describes the
digits of the original number, and an additional part, which indicates the
number's magnitude.

Scientific notation is an abstract concept that could be implemeted in different
ways. The specific format and rules in the memory of computer are specified in
the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) standard.
