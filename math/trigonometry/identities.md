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
    <g stroke="black" stroke-width="0.013" fill="none">
        <path d="M 0.5 0 L 0.866 0.433 0 0.966 Z" stroke-width="0.008" />
        <rect x="0" y="0" width="0.871" height="0.966"   />
    </g>
    <g 
        font-size="0.07"
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
        <text x="0.12" y="0.84">β</text>
        <text x="0.15" y="0.94">α</text>
        <text x="0.83" y="0.31">α</text>
        <text x="0.356" y="0.1">α+β</text>
        <text x="0.25" y="0.4" transform="rotate(-70 0.25 0.4)">1</text>
        <text x="0.5" y="0.7" transform="rotate(-30 0.4 0.7)">cos β</text>
        <text x="0.65" y="0.28" transform="rotate(48 0.65 0.28)">sin β</text>
        <text x="-0.04" y="0.5" transform="rotate(-90 -0.04 0.5)">sin(α+β)</text>
        <text x="0.2" y="-0.03">cos(α+β)</text>
        <text x="0.7" y="-0.03">cos α sin β</text>
        <text x="0.93" y="0.2" transform="rotate(-90 0.93 0.2)">sin α sin β</text>
        <text x="0.93" y="0.7" transform="rotate(-90 0.93 0.7)">sin α cos β</text>
    </g>
    <g fill="none" stroke="black" stroke-width="0.005">
        <path d="M 0.065 0.85 A 0.1 0.1 0 0 1 0.12 0.97" />
        <path d="M 0.067 0.84 A 0.1 0.1 0 0 1 0.122 0.889" />
        <path d="M 0.41 0 A 0.07 0.07 0 0 0 0.465 0.07" />
        <path d="M 0.87 0.32 A 0.07 0.07 0 0 0 0.8 0.35" />
        <path d="M 0.871 0.9 L 0.805 0.9 0.805 0.966" />
        <path d="M 0.805 0 L 0.805 0.065 0.871 0.065" />
        <path d="M 0 0.065 L 0.065 0.065 0.065 0" />
        <path d="M 0.82 0.38 L 0.77 0.42 0.81 0.47" />
    </g>
</svg>

Technically, speaking this figure does not prove identities - it works only for $\alpha, \beta$ that $\alpha + \beta < \pi/2, \alpha < pi/2, \beta < \pi/2$. However, it can be a useful way to remember the identities.
