# Identities

There is a set of trigonometry identities. This page discusses proofs for some of them.

## Sum & Difference

Validity of the identieties:

- $\sin(\alpha + \beta) = \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta)$.
- $\sin(\alpha - \beta) = \sin(\alpha)\cos(\beta) - \cos(\alpha)\sin(\beta)$.

Could be illustrated using following drawing:

<svg width="300" height="360" viewbox="-0.1 -0.1 1 1.2">
    <g>
        <circle cx="0" cy="0" r="0.015" />
        <circle cx="0.5" cy="0" r="0.015" />
        <circle cx="0.866" cy="0" r="0.015" />
        <circle cx="0.866" cy="0.433" r="0.015" />
        <circle cx="0.866" cy="0.966" r="0.015" />
        <circle cx="0" cy="0.966" r="0.015" />
    </g>
    <g stroke="black" stroke-width="0.01" fill="none">
        <path d="M 0.5 0 L 0.866 0.433 0 0.966 Z" stroke-width="0.005" />
        <rect x="0" y="0" width="0.871" height="0.966"   />
    </g>
</svg>

Technically, speaking this figure does not prove identities - it works only for $\alpha, \beta$ that $\alpha + \beta < \pi/2, \alpha < pi/2, \beta < \pi/2$. However, it can be a useful way to remember the identities.
