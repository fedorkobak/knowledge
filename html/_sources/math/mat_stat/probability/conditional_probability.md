# Сonditional probability

Conditional probability is a probability that one event occurs given that other event was occured.

## Basic ideas

Сonditional probability of event A if event B occurs: $P(A \mid B)$.

Conditions $A$ and $B$ independent if: 

$$P(A \mid B)=P(A).$$

The intuition behind this is that if $A$ doesn't depend on $B$, it can occur with the same probability, independently of whether $B$ occurs or not.

Property:

$$\sum_{i=1}^n P(A_i)=1 \Leftrightarrow\sum_{i=1}^nP(A_i \mid B)=1.$$

If $A_i$ are only events that can happen, then one of them will definitely occur even under the $B$ condition.

And a useful practical consequence:

$$P(A \mid B) + P(\overline A \mid B) = 1.$$

## Chain rule

The **chain rule for conditional probability** is the statement:

$$
P(A \mid B) \cdot P(B) = P(A \cap B). \tag{1}
$$

The intuition behind this formula is as follows:

To find the probability that both events $A$ and $B$ occur, we first consider the probability that $B$ occurs, $P(B)$. Then, among the cases where $B$ has occurred, we consider the probability that $A$ also occurs — this is the conditional probability $P(A \mid B)$. Multiplying these two gives the probability that both $A$ and $B$ happen together.

### Even dice

Compute the probability of rolling $2$ with dice, knowing in advance that the dice will return an even number.

This task can be easily solved without any special ideas related to conditional probability. You are interested in rolling $1$ of $3$ possible enven numbers, which can be result of a dice roll, so the probability is $1/3$.

However, you can reach same conclusion by using the Bayes' formula, which clearly shows that it makes sence:

Let's denote: 

- $A$ event that dice roll resulted in even number.
- $B$ event that dice roll resulted in $2$.

Using these definitions, we can write:

- $P(A \cap B)=P(B)=1/6$ as $A \subset B$.
- $P(A) = 1/2$.
- The long statement, "the probability of rolling $2$ with die, knowing in advance that the die iwll return an even number" actually is noting else but $B \mid A$, so we are looking for $P(B \mid A)$.

Using chain rule:

$$P(B \mid A)P(A)=P(A \cap B) \Rightarrow P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1}{3}.$$

The result is the same as when using the basic properties of probability.


## Law of total probability

If we have event $A$ that depends on $n$ events $B_i, i=\overline{(1,n)}$ probability of $A$ can be written as:

$$P(A)=\sum_{i=1}^n P(A \mid B_i)P(B_i)$$

Where $B_i, i=\overline{1,n}$ - events that don't happen at the same time, but one of them will.

### Interesting task

Suppose we have an online shop and we have agreed to support a key partner. In a normal situation, users buy the goods of this partner with a probability of 0.05 (without special displays). If we specially show the product on the homepage, the probability of purchase will be 0.2.

We promised the partner 1000 sales per day, and the traffic per day is 10000 users (one user makes exactly one purchase per day). What is the minimum probability of showing the product on the homepage so that the sales correspond to our agreement?

Let's denote:

- $A$ - user bought the good;
- $B$ - good was shown to the user on the main page.

So:

- We need $1000$ realisations of $A$ in $10000$ events so $P(A) = \frac{1000}{10000}=\frac{1}{10}$;
- The event "we showed good on the main page and it was bought" can be written $A \mid B$, so $P(A|B)=0.2$;
- The event "good bought without being displayed on the main page" can be written as $A \mid \overline B$, so $P(A|\overline B)=0.05$.

And $P(B)$ is our goal.

Using law of total probability we can get:

$$P(A)=P(A \mid B)P(B)+P(A \mid \overline B)P(\overline B) \Rightarrow$$
$$P(A)=P(A \mid B)P(B)+P(A \mid \overline B)[1-P(B)]$$

Is school equation - $P(B)=1/3$.

Interesting that my original solution was slightly different:

Let's denote:

- $x$ - number of users who were shown the good on the main page;
- $y$ - number of users who weren't shown the good on the main page.

Then the system of equations:

$$
\begin{cases}
x+y=10000;\\
0.2*x+0.05*y=1000.
\end{cases}
$$

Which soluton - $x=333, y= 667$. So the final result is $333/10000 = 1/3$.

But it's really the same thing as solution throw law of total probability. Valid expressions:

- $x = P(B)*10000$;
- $y = P(\overline B)*10000.$

Let's substitute them into the system of equations:

$$
\begin{cases}
P(B)*10000+P(\overline B)*10000=10000;\\
0.2*P(B)*10000+0.05*P(\overline B)*10000=1000.
\end{cases}
$$

And divide both equations by $10000$:

$$
\begin{cases}
P(\overline B)=1-P(B);\\
0.2*P(B)+0.05*P(\overline B)=1000/10000.
\end{cases}
$$

We are essentially back to the final expression from the first solution.

## Bayes formula

Consider the expression $(1)$ - it can be written similarly for $B$:

$$P(B \mid A)P(A)=P(A \cap B)$$

So we got that:

$$P(A \mid B)P(B)=P(A \cap B)=P(B \mid A)P(A)$$

From here we can get Bayes formula:

$$P(A \mid B)=\frac{P(B \mid A)P(A)}{P(B)}.$$

### Tasks

To make clearer why we may need bayes formula let's consider few tasks.


#### Borken product

Quite a typical task, but for me every time like a new 0_0.

We've made two batches of the product, and it's known that:

- In the first batch there were 5000 products and the probability of rejection is 0.1;
- In the second batch there were 10000 products and the probability of defect is 0.2.

Suppose we take a random product from random batch. It turned out to be defective. We need to calculate the probability that we took a product from the first batch.

Let:

- $A_i, i=\overline{1,n}$ - probability that detail is taken from batch $i$;
- $B$ is probability that prodcut is broken.

So we have $P(A_1)=5000/15000 = 1/3, P(A_2)=10000/15000=2/3, P(B|A_1)=0.1, P(B|A_2)=0.2$.

And need to find $P(A_1 \mid B)$.

Using Bayes formula $P(A_1 \mid B)=\frac{P(B|A_1)P(A_1)}{P(B)}=0.05$

#### Counterfeit coin

Let's imagine that we have a coin that is 99.9% of cases is regular and in 0.1% of cases counterfeit, i.e. it falls only with an eagle. We tossed this coin 10 times, it fell eagle all 10 times.

What are the chances that this coin was a regular coin?

Let's denote that:

- $A$ - coin is regular;
- $B$ - the coin fell 10 times with an eagle.

So the probability we are looking for is $P(A|B)$ that we got 10 eadgles if the coin is regular. We can find it using the Baues formula:

$$P(A \mid B)=\frac{P(B \mid A)P(A)}{P(B)}.$$

Now using [law of total probability](#Law-of-total-probability) we can rewrite:

$$P(B) = P(B \mid A)P(A) + P(B \mid \overline{A})P(\overline{A});$$

$$P(A \mid B)=\frac{P(B \mid A)P(A)}{P(B \mid A)P(A) + P(B \mid \overline{A})P(\overline{A})}.$$

Based on the condition we can write the following values:

- $P(B \mid A)=0.5^{10}$ - probability of 10 out of 10 eagles for a regular coin;
- $P(A)=0.999$ - given value that coin under consideration is regular;
- $P(\overline{A})=0.001$ - obviously follows from the previous paragraph;
- $P(B \mid \overline{A})=1$ - coin is broken, so it guarantees edgles.

Now we have everything to solve task under consideration:

$$P(A \mid B)=\frac{0.5^{10}0.999}{0.5^{10}0.999 + 0.001} = 0.4938.$$
