# Ranking task

Some sources distinguish the ranking task as a separate class of machine learning tasks.

## Formal task description

Let's denote:
- Set of the abstrac quieries as $Q=\{q_i\}_{i=1}^n$;
- Set of the items as $I=\{i_i\}_{i=1}^m$.

We need to predict target $R=\left[r_{ij}\right]_{n\times m}$, where each $r_{ij}$ represents the importance of the $j$-th item for $i$-th query.