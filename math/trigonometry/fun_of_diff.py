'''
Generate a SVG code that illustrates the sin/cos of difference identity
'''
import pyperclip
import math as m

a = m.pi / 6 + m.pi / 10
b = m.pi / 6

h = m.sin(a) * m.cos(b)
w = m.cos(a - b)
C_y = m.cos(a) * m.sin(b)
E_x = m.cos(a) * m.cos(b)

mul = 0.5
viewbox = f"-0.1 -0.1 {w + mul * w} {h + mul * h}"

alpha_arc = (
    f'<path d="M {m.cos(a) * 0.1} {h - m.sin(a) * 0.1}' +
    f'A 0.1 0.1 0 0 1 0.1 {h}"' +
    '/>'
)
alpha_m_beta_arc = (
    f'<path d="M {m.cos(a - b) * 0.2} {h - m.sin(a - b) * 0.2} ' +
    f'A 0.2 0.2 0 0 1 0.2 {h}" ' +
    '/>'
)
AEF_angle = (
    f'<path d="M {E_x - m.cos(a) * 0.1} {m.sin(a) * 0.1} ' +
    f'A 0.1 0.1 0 0 1 {E_x - 0.1} 0" ' +
    '/>'
)
DCE_angle = (
    f'<path d="M {w} {C_y - 0.1} ' +
    'A 0.1 0.1 1 0 0 ' +
    f'{w + m.cos(m.pi/2 + a) * 0.1} {C_y - m.sin(m.pi/2 + a) * 0.1}" ' +
    '/>'
)

alfa_symbol = (
    f'<text x="{m.cos(a - (b / 2)) * 0.125}" ' +
    f'y="{h - m.sin(a - (b / 2)) * 0.125}">α</text>'
)
beta_symbol = (
    f'<text x="{m.cos(a - (b / 2)) * 0.2}" ' +
    f'y="{h - m.sin(a - (b / 2)) * 0.2}">β</text>'
)
alpha_m_beta_symbol = (
    '<text text-anchor="start" ' +
    f'x="{m.cos((a - b) / 2) * 0.21}" ' +
    f'y="{h - m.sin((a - b) / 2) * 0.21}">α - β' +
    '</text>'
)
AEF_symbol = (
    '<text ' +
    f'x="{E_x - m.cos(a/2) * 0.13}" ' +
    f'y="{m.sin(a/2) * 0.13}" >α' +
    '</text>'
)
ECD_symbol = (
    '<text ' +
    f'x="{w + m.cos(m.pi/2 + a/2) * 0.13}" ' +
    f'y="{C_y - m.sin(m.pi/2 + a/2) * 0.13}" >α' +
    '</text>'
)
hypotenuse_one = (
    f'<text x={w / 2} y={(C_y + h) / 2 - 0.01} ' +
    f'transform="rotate({(-(a - b) * 180 / m.pi)}, {w/2}, {(C_y + h) / 2})" ' +
    'dominant-baseline="Auto">1</text>'
)
AE_distance = (
    f'<text x={h / 2 - 0.02} y={E_x / 2 - 0.02} ' +
    'transform="rotate(' +
    f'{-a * 180 / m.pi}, {h / 2 - 0.02}, {E_x / 2 - 0.02}' +
    ')" ' +
    'dominant-baseline="Auto"' +
    '>cos β</text>'
)
EC_distance = (
    '<text ' +
    f'x={(E_x + w) / 2 + 0.015} y={C_y / 2 - 0.015} ' +
    'transform="rotate(' +
    f'{(m.pi/2 - a) * 180 / m.pi}, '
    f'{(E_x + w) / 2 + 0.015}, {C_y / 2 - 0.015}' +
    ')" ' +
    'dominant-baseline="Auto"' +
    '>sin β</text>'
)
FE_distance = (
    f'<text x={E_x / 2} y=-0.02 dominant-baseline="Auto">cos α cos β</text>'
)
ED_distance = (
    f'<text x={(w + E_x) / 2} y=-0.02 '
    + 'dominant-baseline="Auto">sin α sin β</text>'
)
AF_distance = (
    f'<text x=-0.02 y={h / 2} ' +
    f'transform="rotate(-90, -0.02, {h / 2})" ' +
    'dominant-baseline="Auto"' +
    '>sin α cos β</text>'
)
CD_distance = (
    f'<text x={w + 0.05} y={C_y / 2} ' +
    f'transform="rotate(-90, {w + 0.05}, {C_y / 2})" ' +
    'dominant-baseline="Auto"' +
    '>sin α cos β</text>'
)
BC_distance = (
    f'<text x={w + 0.05} y={(h + C_y) / 2} ' +
    f'transform="rotate(-90, {w + 0.05}, {(h + C_y) / 2})" ' +
    'dominant-baseline="Auto"' +
    '>sin (α - β)</text>'
)
AB_distance = (
    f'<text x={w / 2} y={h + 0.01} dominant-baseline="hanging">' +
    'cos (α - β)</text>'
)


def get_beta_arc(r: float):
    return (
        f'<path d="M {m.cos(a) * r} {h - m.sin(a)*r} ' +
        f'A {r} {r} 0 0 1 {m.cos(a - b) * r} {h - m.sin(a - b) * r}" />'
    )


def get_right_angle(x: float, y: float, d: float, angle: float) -> str:
    p1 = (
        x + m.cos(angle - m.pi / 4) * d,
        y - m.sin(angle - m.pi / 4) * d
    )
    p2 = (
        x + m.cos(angle) * (2**(1/2)) * d,
        y - m.sin(angle) * (2**(1/2)) * d
    )
    p3 = (
        x + m.cos(angle + m.pi / 4) * d,
        y - m.sin(angle + m.pi / 4) * d
    )

    return f'<path d="M {p1[0]} {p1[1]} L {p2[0]} {p2[1]} {p3[0]} {p3[1]}"/>'


pr = 0.012

template = f"""
<svg width="{w * 500}" height="{h * 500}" viewbox="{viewbox}">
    <g>
        <circle cx="0" cy="0" r="{pr}" />
        <circle cx="0" cy="{h}" r="{pr}" />
        <circle cx="{w}" cy="0" r="{pr}" />
        <circle cx="{w}" cy="{h}" r="{pr}" />
        <circle cx="{m.cos(a)*m.cos(b)}" cy="0" r="{pr}" />
        <circle cx="{w}" cy="{C_y}" r="{pr}" />
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
        dominant-baseline="middle"
        style="font-family: 'LatinModern'"
        font-style="italic"
    >
        <text x="0" y="{h + pr}" dominant-baseline="Hanging">A</text>
        <text x="{w}" y="{h + pr}" dominant-baseline="Hanging">B</text>
        <text x="{w + pr}" y="{C_y}" text-anchor="start">C</text>
        <text x="{E_x}" y="{-pr * 2}" dominant-baseline="Auto">E</text>
        <text x="{w}" y="{-pr * 2}" dominant-baseline="Auto">D</text>
        <text x="0" y="{-pr * 2}" dominant-baseline="Auto">F</text>
        {alfa_symbol}
        {beta_symbol}
        {alpha_m_beta_symbol}
        {AEF_symbol}
        {ECD_symbol}
        {hypotenuse_one}
        {AE_distance}
        {FE_distance}
        {ED_distance}
        {EC_distance}
        {AF_distance}
        {CD_distance}
        {BC_distance}
        {AB_distance}
    </g>
    <g fill="none" stroke="black" stroke-width="0.005">
        {alpha_arc}
        {get_beta_arc(0.155)}
        {get_beta_arc(0.165)}
        {alpha_m_beta_arc}
        {AEF_angle}
        {DCE_angle}
        {get_right_angle(x=0, y=0, d=0.05, angle=-(m.pi / 4))}
        {get_right_angle(x=w, y=0, d=0.05, angle=(m.pi + m.pi / 4))}
        {get_right_angle(x=w, y=h, d=0.05, angle=(m.pi - m.pi / 4))}
        {get_right_angle(x=E_x, y=0, d=0.05, angle=(m.pi + a + m.pi/4))}
    </g>
</svg>
""".strip()

pyperclip.copy(template)
print(template)
