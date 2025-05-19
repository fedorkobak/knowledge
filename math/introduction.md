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
| Imaginary numbers   | —      | Multiples of $i4 (where $i^2 = -1$)               | $i, 2i, −3i$                              |
| Complex numbers     | $\mathbb{Q}$      | Numbers of form a + bi (a, b ∈ ℝ)            | $2 + 3i, −1 − i, 4$                       |

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

## Statistical testing

**Statistical testing** is a formal procedure used to determine whether there is enough evidence in a sample of data to infer that a certain condition holds for the entire population.

In practice, it involves:

1. **Formulating hypotheses**:

   * The **null hypothesis** ($H_0$): a default assumption (e.g., "no effect", "no difference").
   * The **alternative hypothesis** ($H_1$ or $H_a$): the assertion you want to test (e.g., "there is an effect").

2. **Calculating a test statistic** from the data that summarizes the difference between what is observed and what is expected under the null hypothesis.

3. **Determining a p-value**, which tells you the probability of obtaining a result at least as extreme as the observed one, assuming the null hypothesis is true.

4. **Making a decision**:

   * If the p-value is below a predefined threshold (commonly 0.05), reject the null hypothesis.
   * Otherwise, do not reject it.

Statistical testing is widely used in scientific research, quality control, medicine, and many other fields.

Check more on statistical testing on the [corresponding page](stat_testing.ipynb).


## Central limit theorem

Here’s the improved version of your text:

The formulation of the central limit theorem is:

Let’s take $N$ **independent** values $x_i$ drawn from the same distribution with expected value $\mu$ and standard deviation $\sigma$.

We denote their sum as:

$S_N = \sum_{i=1}^N x_i$

The central limit theorem states that $S_N \sim \mathcal{N}(\mu N, \sigma^2 N)$ — that is, $S_N$ follows a normal distribution with mean $\mu N$ and variance $\sigma^2 N$.

Check more details in the [corresponding page](cent_limit_theorem.ipynb).
