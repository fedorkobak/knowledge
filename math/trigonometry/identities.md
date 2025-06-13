# Identities

There is a set of trigonometry identities. This page discusses proofs for some of them.

## Sum & Difference

### Sum

Validity of the identieties:

- $\sin(\alpha + \beta) = \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta)$.
- $\cos(\alpha + \beta) = \cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta)$.

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
        font-size="0.06"
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
        <text x="0.7" y="-0.03">sin α sin β</text>
        <text x="0.93" y="0.2" transform="rotate(-90 0.93 0.2)">cos α sin β</text>
        <text x="0.93" y="0.7" transform="rotate(-90 0.93 0.7)">sin α cos β</text>
        <text x="0.45" y="1.03">cos α cos β</text>
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

Step-by-step breakdown of this drawing:

1. Draw a right triangle $\Delta ABC$ with an angle of $\angle BAC = \beta$ and a hypotenuse of length 1. The cathetes of this triangle are equal to $\sin(\beta)$ and $\cos(\alpha)$.
2. Draw rectangle $AFED$ around a triangle $ABC$ so that $\angle CAD = \alpha$.
3. Using the properties of parallel lines:
    - $\angle FBA = \angle BAC + \angle CAD = \beta + \alpha$.
    - $\angle CAD = \angle BCE = \alpha$.
4. Consider the triangle $\Delta AFB$. Using the definitions of sine and cosine:
    - $AF=\sin{(\alpha + \beta)}$.
    - $FB=\cos{(\alpha + \beta)}$.
5. Consider the triangle $\Delta BEC$. Using the definitions of sine and cosine:
    - $BE = \sin{\alpha} \sin{\beta}$.
    - $CE = \cos{\alpha} \sin{\beta}$.
6. Consider the triangle $\Delta ACD$. Using the definitions of sine and cosine:
    - $CD = \sin{\alpha} \cos{\beta}$.
    - $AD = \cos{\alpha} \cos{\beta}$.

Finally, using the properties of rectangle:

- $AF = ED \Rightarrow \sin{(\alpha + \beta)} = \cos{\alpha} \sin{\beta} + \sin{\alpha} \cos{\beta}$.
- $FE = AD \Rightarrow \cos{(\alpha + \beta)} + \sin{\alpha}\cos{\beta} = \cos{\alpha}\cos{\beta} \Rightarrow \cos{(\alpha + \beta)} = \cos{\alpha}\sin{\beta} - \sin{\alpha}\cos{\beta}$.

Technically, speaking this figure does not prove identities - it works only for $\alpha, \beta$ that $\alpha + \beta < \pi/2, \alpha < pi/2, \beta < \pi/2$. However, it can be a useful way to remember the identities.

### Difference

Validity of identities:

- $\sin(\alpha - \beta) = \sin(\alpha)\cos(\beta) - \cos(\alpha)\cos(\beta)$.
- $\cos(\alpha - \beta) = \cos(\alpha)\cos(\beta) + \sin(\alpha)\cos(\beta)$.

Could be illustrated using following drawing:

<svg width="554.327719506772" height="412.2384881216701" viewbox="-0.1 -0.1 1.38581929876693 1.0305962203041752">
    <g>
        <circle cx="0" cy="0" r="0.012" />
        <circle cx="0" cy="0.6870641468694502" r="0.012" />
        <circle cx="0.9238795325112867" cy="0" r="0.012" />
        <circle cx="0.9238795325112867" cy="0.6870641468694502" r="0.012" />
        <circle cx="0.5272028623656693" cy="0" r="0.012" />
        <circle cx="0.9238795325112867" cy="0.3043807145043603" r="0.012" />
    </g>
    <path
        d="M 0 0 L 0 0 0 0.6870641468694502 0.9238795325112867 0.6870641468694502 0.9238795325112867 0 Z"
        fill="none" stroke-width="0.01" stroke="black"
    />
    <g stroke="black" stroke-width="0.007">
        <line x1="0" y1="0.6870641468694502" x2="0.9238795325112867" y2="0.3043807145043603" />
        <line x1="0.5272028623656693" y1="0" x2="0.9238795325112867" y2="0.3043807145043603" />
        <line x1="0" y1="0.6870641468694502" x2="0.5272028623656693" y2="0" />
    </g>
    <g
        font-size="0.06"
        text-anchor="middle"
        dominant-baseline="middle"
        style="font-family: 'LatinModern'"
        font-style="italic"
    >
        <text x="0" y="0.6990641468694502" dominant-baseline="Hanging">A</text>
        <text x="0.9238795325112867" y="0.6990641468694502" dominant-baseline="Hanging">B</text>
        <text x="0.9358795325112867" y="0.3043807145043603" text-anchor="start">C</text>
        <text x="0.5272028623656693" y="-0.024" dominant-baseline="Auto">E</text>
        <text x="0.9238795325112867" y="-0.024" dominant-baseline="Auto">D</text>
        <text x="0" y="-0.024" dominant-baseline="Auto">F</text>
        <text x="0.09916916753640441" y="0.6109689682433601">α</text>
        <text x="0.15867066805824706" y="0.565311861067706">β</text>
        <text text-anchor="start" x="0.2059649088846784" y="0.6460951792460632">α - β</text>
        <text x="0.41060940596641976" y="0.057497529728470165" >α</text>
        <text x="0.8663820027828166" y="0.18778725810511077" >α</text>
    </g>
    <g fill="none" stroke="black" stroke-width="0.005">
        <path d="M 0.060876142900872066 0.6077288128403266A 0.1 0.1 0 0 1 0.1 0.6870641468694502"/>
        <path d="M 0.0943580214963517 0.5640943791243087 A 0.155 0.155 0 0 1 0.14320132753924944 0.6277482148528613" />
        <path d="M 0.10044563578643892 0.5561608457213963 A 0.165 0.165 0 0 1 0.15244012286436232 0.6239213805292103" />
        <path d="M 0.18477590650225736 0.6105274603964322 A 0.2 0.2 0 0 1 0.2 0.6870641468694502" />
        <path d="M 0.4663267194647972 0.07933533402912352 A 0.1 0.1 0 0 1 0.4272028623656693 0" />
        <path d="M 0.9238795325112867 0.20438071450436027 A 0.1 0.1 1 0 0 0.8445441984821632 0.24350457160348818" />
    </g>
</svg>
