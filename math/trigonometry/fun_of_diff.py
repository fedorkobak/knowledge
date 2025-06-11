import math as m
a = m.pi/8 + m.pi/5
b = m.pi/8

h = m.sin(a)*m.cos(a)
w = m.cos(a - b)

mul = 0.5
viewbox = f"-0.1 -0.1 {w + mul * w} {h + mul * h}"

template = f"""
<svg width="{w * 600}" height="{h * 600}" viewbox="{viewbox}">
    <g>
        <circle cx="0" cy="0" r="0.012" />
        <circle cx="0" cy="{h}" r="0.012" />
        <circle cx="{w}" cy="0" r="0.012" />
        <circle cx="{w}" cy="{h}" r="0.012" />
        <circle cx="{m.cos(a)*m.cos(b)}" cy="0" r="0.012" />
        <circle cx="{w}" cy="{m.cos(a)*m.sin(b)}" r="0.012" />
    </g>
    <path
        d="M 0 0 L 0 0 0 {h} {w} {h} {w} 0 Z"
        fill="none" stroke-width="0.01" stroke="black"
    />
</svg>
"""

print(template)
