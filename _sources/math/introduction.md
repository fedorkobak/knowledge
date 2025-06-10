# Intorduction

This section deals with ideas from mathematics that I found useful.

## Sets of numbers

| Name               | Symbol | Definition                                    | Examples                                  |
|---------------------|--------|----------------------------------------------|------------------------------------------|
| Natural numbers     | $\mathbb{N}$      | Counting numbers (sometimes includes 0)       | $1, 2, 3, 4, 5, …$ |
| Whole numbers       | —      | Natural numbers plus zero                     | $0, 1, 2, 3, 4, 5, …$                     |
| Integers           | $\mathbb{Z}$      | Whole numbers plus negatives                  | $…, −3, −2, −1, 0, 1, 2, 3, …$            |
| Rational numbers    | $\mathbb{Q}$      | Fractions of integers                        | $1/2, −4/3, 7$               |
| Irrational numbers  | —      | Cannot be expressed as a fraction            | $\sqrt{2}, \pi$                              |
| Real numbers        | $\mathbb{R}$      | All rational and irrational numbers          | Any point on the number line             |
| Imaginary numbers   | —      | Multiples of $i$ (where $i^2 = -1$)               | $i, 2i, −3i$                              |
| Complex numbers     | $\mathbb{Q}$      | Numbers of form a + bi (a, b ∈ ℝ)            | $2 + 3i, −1 − i, 4$                       |

## Square root

The square root of a number $x$ is the number $y$ such that $x=y^2$.

By definition of the square root, it always have to have two solutions. Since any pair of opposite numbers (i.e., $a = -b$) satisfy $a^2 = b^2$, squaring each yields the same result. 

### Principal square root ($\sqrt{}$)

**The principal square root** (rus. арифметический корень) is the **nonnegative** square root of a number.

Principal suqre root usually denoted as:

$$y = \sqrt{x}.$$

**Note:** The symbol $\sqrt{}$ is called a **radical**.

**Note:** It's common to use the term "square root" when refferting to the principal square root. Remember that the notation $\sqrt{x}$ refers to the principal square root.

It follows that when you are solving equation like:

$$y = x^2.$$

Remeber that the expression $\sqrt{y}$ will correspond to $x$ value in both signs:

$$x = \pm \sqrt{x}.$$

## Quadratic function

Consider a function of the form:

$$
f(x) = ax^2 + bx + c \quad \text{where } a, b, c \in \mathbb{Q}, a \neq 0
$$

This function is called a "quadratic function".

A common practical task is to find the values of $x$ for which $f(x) = 0$. The corresponding equation is called quadratic and is displayed explicitly below:

$$
ax^2 + bx + c = 0 \quad \text{where } a, b, c \in \mathbb{Q}, a \neq 0
$$

### Equation solution

Multiply the equation to $1/a$:

$$
x^2 + \frac{b}{a}x + \frac{c}{a} = 0
$$

Perform the following sequence of transformations to apply the sum-of-squares formula:

$$x^2 + 2\frac{b}{2a}x + \left( \frac{b}{2a} \right)^2 - \left( \frac{b}{2a}\right)^2 + \frac{c}{a} = 0$$

$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2}{4a^2} - \frac{c}{a}$$

$$x + \frac{b}{2a} = \pm\sqrt{\frac{b^2 - 4ac}{4a^2}}$$

Take a closer look at the expression on the right side of the equation:

$$\pm\frac{\sqrt{b^2 - 4ac}}{2 |a|}$$

Expression $\pm|a| = \pm a$ is correct as a concise way to represent that $|a|$ and $a$ differ only in sign, and both $\pm|a|$ and $\pm a$ denote the set of two numbers: $a$ and $-a$. So:

$$x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 -4ac}}{2a}$$

Finally, both solutions to the equation can be expressed as follows:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

The expression $b^2 - 4ac$ is called the descrimimnant of a quadratic equation and is denoted by $D$. Obviously, $D\geq0$ for there to be solutions in the rational numbers.

## Logarithm

Logarithm of a number $x$ with base $a$ is the number $y$ such that $a^y = x$.
The logarithm of $x$ with base $a$ is denoted as $\log_a(x)$.

### Restrictions

The logarithm is defined only in the following cases:

$$
\begin{cases}
   x > 0; \\
   a \neq 1; \\
   a > 0.
\end{cases}
$$

$a \neq 1$, since $1^y = 1$ for all real numbers $y$. So for this case the function cannot be defined uniquely.

$0^y = 0$ for all $y \geq 0$ and not defined for $y < 0$. So for this case the function cannot be defined uniquely.

If $a < 0$, $a^y$ changes the sign for even and odd values of $y$. Therefore, for sertain values of $x$, it is impossible to find such $y$ that corresponds to the $\log_a x$.

As $a > 0$ it powerd to any number will return positive number - $a^y > 0 \Rightarrow x>0$.


**Note:** You can find such $x < 0, a < 0$ that the logarithm is correct by definition, e.g. $\log_{-2} -8 = 3$. However, it is difficult to use such logarithms in applications, se there is an argeement that $x > 0$ and $a > 0$.

## Arithmetic progression

An arithmetic progression is a sequence of numbers in which each element differs from the previous one by a constant amount.

Let's denote:

- $a_1$: the fist element of an arithmetic progression.
- $d$: difference of an arithmetic progression.

By definition, each element of the progression can be counted as:

$$a_i = a_{i-1} + d, i=\overline{2,n}$$

The sequence also can be written using only $a_1$ and $d$.

$$a_1, a_1 + d, a_1 + 2d, ...$$

This leads to a more useful formula:

$$a_n = a_1 + (n-1)d$$

### Sum

Finding a sum of the first $n$ members of an arithmetic progression is a very typical task. There is no issues to compute it by hands but there is a better approach - formula for $S_n$:

$$S_n = \frac{n(a_1 + a_n)}{2}$$

To prove this formula, write the sum in the expanded form:

$$S_n = a_1 + (a_1 + d) + (a_1 + 2d) + \ldots + (a_1 + [n-1]d).$$

And the same sum in the reverse order:

$$S_n = (a_1 + [n-1]d) + (a_1 + [n-2]d) + \ldots + a_1.$$

Now, add those two sums together and group the :

$$2S_n = (2a_1 + [n-1]d) + (2a_1 + d + [n-2]d) + \ldots + (2a_1 + d + [n-2]d) + (2a_1 +[n-1]d).$$
$$S_n = \frac{n(a_1 + a_1 + [n-1]d)}{2}.$$

Finally as $a_n = a_1 + [n-1]d$:

$$S_n = \frac{n(a_1 + a_n)}{2}.$$

## Trigonometry

Trigonometry is a branch of mathematics that studies the relationships between the angles and sides of triangles, especially right-angled triangles.

There are three main functions in trigonometry:

- sine: $sin(\theta)$.
- cosine: $cos(\theta)$.
- tangent: $tan(\theta)$. 

The following cell shows the most common values of the trigonometric functions.

| Angle (°) | Angle (rad)         | $\sin(\theta)$        | $\cos(\theta)$        | $\tan(\theta)$        |
| --------- | ------------------- | ----------------------- | ----------------------- | ----------------------- |
| 0°        | $0$               | $0$                   | $1$                   | $0$                   |
| 30°       | $\frac{\pi}{6}$   | $\frac{1}{2}$         | $\frac{\sqrt{3}}{2}$  | $\frac{1}{\sqrt{3}}$  |
| 45°       | $\frac{\pi}{4}$   | $\frac{\sqrt{2}}{2}$  | $\frac{\sqrt{2}}{2}$  | $1$                   |
| 60°       | $\frac{\pi}{3}$   | $\frac{\sqrt{3}}{2}$  | $\frac{1}{2}$         | $\sqrt{3}$            |
| 90°       | $\frac{\pi}{2}$   | $1$                   | $0$                   | undefined               |
| 120°      | $\frac{2\pi}{3}$  | $\frac{\sqrt{3}}{2}$  | $-\frac{1}{2}$        | $-\sqrt{3}$           |
| 135°      | $\frac{3\pi}{4}$  | $\frac{\sqrt{2}}{2}$  | $-\frac{\sqrt{2}}{2}$ | $-1$                  |
| 150°      | $\frac{5\pi}{6}$  | $\frac{1}{2}$         | $-\frac{\sqrt{3}}{2}$ | $-\frac{1}{\sqrt{3}}$ |
| 180°      | $\pi$             | $0$                   | $-1$                  | $0$                   |
| 210°      | $\frac{7\pi}{6}$  | $-\frac{1}{2}$        | $-\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}}$  |
| 225°      | $\frac{5\pi}{4}$  | $-\frac{\sqrt{2}}{2}$ | $-\frac{\sqrt{2}}{2}$ | $1$                   |
| 240°      | $\frac{4\pi}{3}$  | $-\frac{\sqrt{3}}{2}$ | $-\frac{1}{2}$        | $\sqrt{3}$            |
| 270°      | $\frac{3\pi}{2}$  | $-1$                  | $0$                   | undefined               |
| 300°      | $\frac{5\pi}{3}$  | $-\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$         | $-\sqrt{3}$           |
| 315°      | $\frac{7\pi}{4}$  | $-\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$  | $-1$                  |
| 330°      | $\frac{11\pi}{6}$ | $-\frac{1}{2}$        | $\frac{\sqrt{3}}{2}$  | $-\frac{1}{\sqrt{3}}$ |
| 360°      | $2\pi$            | $0$                   | $1$                   | $0$                   |
