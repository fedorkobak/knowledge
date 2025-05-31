# Identities

There is a set of trigonometry identities. This page discusses proofs for some of them.

## Sum & Difference

Validity of the identieties:

- $\sin(\alpha + \beta) = \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta)$.
- $\sin(\alpha - \beta) = \sin(\alpha)\cos(\beta) - \cos(\alpha)\sin(\beta)$.

Could be illustrated using following drawing:

<svg width="330" height="360" viewbox="-0.1 -0.1 1.1 1.2">
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
    <g 
        font-size="0.08"
        text-anchor="middle"
        style="font-family: 'LatinModern'"
        font-style="italic"
    >
        <text x="-0.04" y="0" >F</text>
        <text x="0.5" y="-0.02">B</text>
        <text x="0.91" y="0">E</text>
        <text x="0.91" y="0.45">C</text>
        <text x="0.91" y="1">D</text>
        <text x="-0.04" y="1">A</text>
    </g>
</svg>

Technically, speaking this figure does not prove identities - it works only for $\alpha, \beta$ that $\alpha + \beta < \pi/2, \alpha < pi/2, \beta < \pi/2$. However, it can be a useful way to remember the identities.
