# Recommendation systems

Recommendation systems is really popular application of the machine learning. These algorithms match some items to some users.

## Formal task description

Let's denote: 
- Set of the users as $U=\{u_i\}_{i=1}^n$;
- Set of the items as $I=\{i_i\}_{i=1}^m$.

We need to predict target $R=\left[r_{ij}\right]_{n\times m}$, where each $r_{ij}$ represents the importance of the $j$-th item for $i$-th client.