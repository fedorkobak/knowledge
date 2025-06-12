import pyperclip
import math as m

a = m.pi/6 + m.pi/8
b = m.pi/6

h = m.sin(a)*m.cos(b)
w = m.cos(a - b)
C_y = m.cos(a)*m.sin(b)
E_x = m.cos(a)*m.cos(b)

mul = 0.5
viewbox = f"-0.1 -0.1 {w + mul * w} {h + mul * h}"

template = f"""
<svg
    width="{w * 600}" height="{h * 600}"
    viewbox="{viewbox}">
    <g>
        <circle cx="0" cy="0" r="0.012" />
        <circle cx="0" cy="{h}" r="0.012" />
        <circle cx="{w}" cy="0" r="0.012" />
        <circle cx="{w}" cy="{h}" r="0.012" />
        <circle cx="{m.cos(a)*m.cos(b)}" cy="0" r="0.012" />
        <circle cx="{w}" cy="{C_y}" r="0.012" />
    </g>
    <path
        d="M 0 0 L 0 0 0 {h} {w} {h} {w} 0 Z"
        fill="none" stroke-width="0.01" stroke="black"
    />
    <g stroke="black" stroke-width="0.007">
        <line x1="{0}" y1="{h}" x2="{w}" y2="{C_y}" />
        <line x1="{m.cos(a)*m.cos(b)}" y1="0" x2="{w}" y2="{C_y}" />
        <line x1="0" y1="{h}" x2="{E_x}" y2="0" />
    </g>
    <g
        font-size="0.06"
        text-anchor="middle"
        style="font-family: 'LatinModern'"
        font-style="italic"
    >
        <text x="0" y="{h + 0.07}">A</text>
        <text x="{w}" y="{h + 0.07}">B</text>
        <text x="{w + 0.04}" y="{C_y + 0.02}">C</text>
        <text x="{E_x}" y="-0.03">E</text>
        <text x="{w}" y="-0.03">D</text>
        <text x="0" y="-0.03">F</text>
        <text
            x="{m.cos(a / 2) * 0.1 + 0.01}"
            y="{h - m.sin(a / 2) * 0.1 - 0.01}">α</text>
    </g>
    <g fill="none" stroke="black" stroke-width="0.005">
        <path
            d="M {m.cos(a)*0.1} {h - m.sin(a)*0.1}
            A 0.1 0.1 0 0 1 0.1 {h}" />
    </g>
</svg>
""".strip()

pyperclip.copy(template)
print(template)
