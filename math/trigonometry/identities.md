# Identities

There is a set of trigonometry identities. This page discusses proofs for some of them.

## Sum & Difference

### Sum

Validity of the identieties:

- $\sin(\alpha + \beta) = \sin{\alpha} \cos {\beta} + \cos{\alpha} \sin{\beta}$.
- $\cos(\alpha + \beta) = \cos{\alpha}\cos{\beta} - \sin{\alpha}\sin{\beta}$.

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

<svg width="475.52825814757676" height="321.79114877718825" viewbox="-0.1 -0.1 1.4265847744427302 0.9653734463315646">
    <g>
        <circle cx="0" cy="0" r="0.012" />
        <circle cx="0" cy="0.6435822975543765" r="0.012" />
        <circle cx="0.9510565162951535" cy="0" r="0.012" />
        <circle cx="0.9510565162951535" cy="0.6435822975543765" r="0.012" />
        <circle cx="0.5794841035564565" cy="0" r="0.012" />
        <circle cx="0.9510565162951535" cy="0.33456530317942906" r="0.012" />
    </g>
    <path
        d="M 0 0 L 0 0 0 0.6435822975543765 0.9510565162951535 0.6435822975543765 0.9510565162951535 0 Z"
        fill="none" stroke-width="0.01" stroke="black"
    />
    <g stroke="black" stroke-width="0.007">
        <line x1="0" y1="0.6435822975543765" x2="0.9510565162951535" y2="0.33456530317942906" />
        <line x1="0.5794841035564565" y1="0" x2="0.9510565162951535" y2="0.33456530317942906" />
        <line x1="0" y1="0.6435822975543765" x2="0.5794841035564565" y2="0" />
    </g>
    <g
        font-size="0.06"
        text-anchor="middle"
        dominant-baseline="middle"
        style="font-family: 'LatinModern'"
        font-style="italic"
    >
        <text x="0" y="0.6615822975543765" dominant-baseline="Hanging">A</text>
        <text x="0.9510565162951535" y="0.6615822975543765" dominant-baseline="Hanging">B</text>
        <text x="0.9630565162951535" y="0.33456530317942906" text-anchor="start">C</text>
        <text x="0.5794841035564565" y="-0.024" dominant-baseline="Auto">E</text>
        <text x="0.9510565162951535" y="-0.024" dominant-baseline="Auto">D</text>
        <text x="0" y="-0.024" dominant-baseline="Auto">F</text>
        <text x="0.104833820993178" y="0.5755024181774981">α</text>
        <text x="0.16773411358908483" y="0.534654490551371">β</text>
        <text text-anchor="start" x="0.20741455152497892" y="0.610731059895928">α - β</text>
        <text x="0.4607231940629184" y="0.05287576359985402" >α</text>
        <text x="0.8981807526952995" y="0.21580439368589094" >α</text>
        <text x=0.47552825814757677 y=0.4790738003669027 transform="rotate(-18.0, 0.47552825814757677, 0.48907380036690273)" dominant-baseline="Auto">1</text>
        <text x=0.3017911487771882 y=0.26974205177822824 transform="rotate(-48.0, 0.3017911487771882, 0.26974205177822824)" dominant-baseline="Auto">cos β</text>
        <text x=0.28974205177822826 y=-0.02 dominant-baseline="Auto">cos α cos β</text>
        <text x=0.765270309925805 y=-0.02 dominant-baseline="Auto">sin α sin β</text>
        <text x=0.780270309925805 y=0.15228265158971455 transform="rotate(42.0, 0.780270309925805, 0.15228265158971455)" dominant-baseline="Auto">sin β</text>
        <text x=-0.02 y=0.32179114877718823 transform="rotate(-90, -0.02, 0.32179114877718823)" dominant-baseline="Auto">sin α cos β</text>
        <text x=1.0010565162951535 y=0.16728265158971453 transform="rotate(-90, 1.0010565162951535, 0.16728265158971453)" dominant-baseline="Auto">cos α sin β</text>
        <text x=1.0010565162951535 y=0.48907380036690273 transform="rotate(-90, 1.0010565162951535, 0.48907380036690273)" dominant-baseline="Auto">sin (α - β)</text>
        <text x=0.47552825814757677 y=0.6535822975543765 dominant-baseline="hanging">cos (α - β)</text>
    </g>
    <g fill="none" stroke="black" stroke-width="0.005">
        <path d="M 0.06691306063588583 0.569267815006637A 0.1 0.1 0 0 1 0.1 0.6435822975543765"/>
        <path d="M 0.10371524398562303 0.5283948496053804 A 0.155 0.155 0 0 1 0.1474137600257488 0.5956846634262596" />
        <path d="M 0.11040655004921161 0.5209634013506064 A 0.165 0.165 0 0 1 0.15692432518870034 0.5925944934825101" />
        <path d="M 0.1902113032590307 0.581778898679387 A 0.2 0.2 0 0 1 0.2 0.6435822975543765" />
        <path d="M 0.5125710429205707 0.07431448254773941 A 0.1 0.1 0 0 1 0.47948410355645654 0" />
        <path d="M 0.9510565162951535 0.23456530317942906 A 0.1 0.1 1 0 0 0.8767420337474141 0.26765224254354325" />
        <path d="M 3.061616997868383e-18 0.05 L 0.05000000000000002 0.05 0.05 0.0"/>
        <path d="M 0.9010565162951535 -6.123233995736766e-18 L 0.9010565162951535 0.05 0.9510565162951535 0.05"/>
        <path d="M 0.9510565162951535 0.5935822975543764 L 0.9010565162951535 0.5935822975543764 0.9010565162951535 0.6435822975543765"/>
        <path d="M 0.5460275732385136 0.03715724127386972 L 0.5831848145123834 0.07061377159181263 0.6166413448303263 0.033456530317942906"/>
    </g>
</svg>

There is a right triangle $AEC$ with $\angle AEC = \frac{\pi}{2}$ and hypotenuse $AC=1$, inscribed in the triangle $AFDB$ such that $E$ lies on $FD$, $C$ lies on $BD$ and $\angle EAC = \alpha$.

To see correctness of sin/cos difference formulas follow the logic:

- Due to the definitions of sine and cosine: $AE = \sin{\beta}$ and $EC = \cos{\beta}$.
- Using the properties of parallel lines $AB$ and $FD$: $\angle AEF = \angle BEA \Rightarrow \angle AEF = \alpha$.
- Due to the properties of the right angle triangles and the definition of trigonometric functions:
  - For triangle $AFE$: $AF = \sin{\alpha}\cos{\beta}$, $EF = \cos{\alpha}\cos{\beta}$.
  - For triangle $EDC$: $ED = \sin{\alpha}\sin{\beta}$, $CD = \sin{\alpha}cos{\beta}$.
- Since $\angle ABC = \angle EAB - \angle EAC$: $\angle EAC = \alpha - \beta$. Finally:
  - For triangle $ABC$: $BC=\sin{(\alpha - \beta)}$, $AB=\cos{(\alpha - \beta)}$.

Finally, using properties of the rectangle:

- $AB = FE + ED \Rightarrow \cos{(\alpha - \beta)} = \cos{\alpha} \cos{\beta} + \sin{\alpha} \sin{\beta}$
- $AF = BC + CD \Rightarrow \sin{\alpha}\cos{\beta} = \sin{(\alpha - \beta)} + \cos{\alpha} \sin{\beta} \Rightarrow \sin{(\alpha - \beta)} = \sin{\alpha}\cos{\beta} - \cos{\alpha}\sin{\beta}$.
