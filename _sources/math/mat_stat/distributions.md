# Distributions

The distribution is a rule that describes the probability of different outcomes of an experiment.

## Bernoulli

The Bernoulli distribution describes the experiments with binary outcomes.

Denote the outcomes as either positive or negative. Lets encode cases: 

$$x = \begin{cases}
0, & negative, \\
1, & positive.
\end{cases}$$

The main parameter of the distribution is $p$, which is the probability that outcome of the random value will be positive. The rule can then be written as follows: $x$ takes value 1 with probability $p$ and the value 2 with probability $1 - p$.

More formally probability mass function:

$$f(x) = p^{x}(1-p)^{(1-x)}$$

Meaning is simple: $f(1) = p^1(1-p)^0 = p$ and $f(0) = p^0(1-p)^1 = 1 - p$.

## Normal Distribution

The **normal distribution**, also known as the **Gaussian distribution**, is a 
continuous probability distribution characterized by its bell-shaped curve. 
It is defined by two parameters:

- **Mean ($\mu$)**: the center of the distribution.
- **Standard deviation ($\sigma$)**: controls the spread of the data.

Its probability density function (PDF) is given by:

$$
f(x \mid \mu, \sigma^2) = \frac{1}{\sigma \sqrt{2\pi}}
\exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
$$

The normal distribution is widely used in statistics and machine learning 
because many natural phenomena and measurement errors tend to follow it.
