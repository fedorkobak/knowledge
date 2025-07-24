# Probability

Probability is a function of an event. It has a few interesting and useful properties that we will consider on this page.

## Union probability

The sum rule for joint events describes the probability that at least one of the events will occur. It's a bit of a confusing rule - it's really common for me to make mistakes in problems involving this rule.

### Definition

Let we have $A$ event and $B$ event.

If $A$ and $B$ occur at the same time, we denote it by the intersection of the events $A \cap B$.

If at least one of the events $A$ and $B$ occurs, we denote it as a union of events $A \cup B$.

The probabilities of all events are related by the formula:

$$P(A\cup B)=P(A)+P(B)-P(A \cap B)$$

Sometimes it can be confusing that you need to know the probability that events will occur at the same time to calculate the probability that at least one will occur. But think about it more careful - individual probabilities do not contain any information about how often these events occur together, so how often these events occur together must be learnt separately.

### Example task

In my practice I have come across really simple tasks that can be solved using this rule.

There are two options for building a shop: one large shop or two small shops. The large shop will succeed with a probability of 2 times that of the small one, the small ones act independently (i.e. it can succeed either one or the other, or both at once, with success events being independent).

Which is more favourable to do? We consider that success is important to us, for two small ones it doesn't matter whether one or both of them "shoot".

Let's designate:

- $a$ - case where small shop was successful;
- $A$ - case where big shop was successful.

So to solve the task we need to compare $P(A)$ and $P(a \cup a)$.

From the problem condition: $P(A)=2P(a)$.

And using rule for joint events: $P(a\cup a) = P(a) + P(a) - P(a\cap a)=2P(a) - P(a \cap a)$.

So now we are comparing $2P(a)$ and $2P(a) - P(a \cap a)$. 

Obviously $P(a \cap a) > 0$ so finally:

$$2P(a) > 2P(a) - P(a \cap a) \Leftrightarrow P(A) > P(a \cap a).$$

So it's better to open one big store than two small.


## Conditional probability

Conditional probability is a probability that one event occurs given that other event was occured.

In event notation, the occurrence of event $A$ given the occurrence of event $B$ is usually denoted as $A \vert B$. Therefore, the conditional probability is denoted as $P(A \vert B)$.

There are a few key identities related to conditional probabilities:

* If events $A$ and $B$ are independent, then $P(A \mid B) = P(A)$.
* **Law of Total Probability**: If event $A$ depends on a partition of the sample space into events $B_i, \ i = 1, \dots, n$, then

  $$
  P(A) = \sum_{i=1}^n P(A \mid B_i) P(B_i).
  $$
* **The chain rule** states that the probability of two events $A$ and $B$ occurring simultaneously equals the conditional probability of $B$ given $A$ multiplied by the probability of $A$:

  $$
  P(B \cap A) = P(B \mid A) P(A).
  $$

For more details check [conditional probability](probability/conditional_probability.md) page.
