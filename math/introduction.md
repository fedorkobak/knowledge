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
