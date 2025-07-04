from typing import Callable
template = """
<svg width=700 height=200 stroke="black" stroke-width="3"
    style="font-family: 'LatinModern'" font-style="italic" font-size=30>
  <line x1=0 y1=150 x2=600 y2=150 />
  <line x1=600 y1=150 x2=570 y2=160 />
  <line x1=600 y1=150 x2=570 y2=140 />
  <g stroke-width="2">
    {lines}
    <g stroke-dasharray="4">
    {projections}
    </g>
  </g>
  {circles}
  <g stroke-width=0>
    <text x=580 y=180>t</text>
    {coord_denotes}
  </g>
</svg>
"""

coordinates = [(30, 130), (160, 300), (190, 480), (320, 440), (350, 530)]
coordinates.sort()


lines: list[str] = []
line_template = "<line x1={x1} y1={y} x2={x2} y2={y} />"
circles: list[str] = []
circle_template = "<circle cx={x} cy={y} r=2 />"
projections: list[str] = []
projection_template = "<line x1={x} y1={y} x2={x} y2=150 />"
coord_denote: Callable[[int, int, str], str] = lambda x, i, text: (
    f"<text x={x} y=175>{text}</text>"
    f"<text x={x + 10} y=180 font-size=15>{i}</text>"
)
coord_denotes: list[str] = []

y_postions = [(130, 0),]

for i, (begin, end) in enumerate(coordinates):

    # Mechanism that assigns y positions
    y_coord = None
    for j, (y, border) in enumerate(y_postions):
        if begin > border:
            y_coord = y
            y_postions[j] = (y, end)
            break
    if y_coord is None:
        y_coord = y_postions[-1][0] - 20
        y_postions.append((y_coord, end))

    lines.append(line_template.format(x1=begin, y=y_coord, x2=end))
    circles.append(circle_template.format(x=begin, y=y_coord))
    circles.append(circle_template.format(x=end, y=y_coord))
    projections.append(projection_template.format(x=begin, y=y_coord))
    projections.append(projection_template.format(x=end, y=y_coord))
    coord_denotes.append(coord_denote(x=begin - 5, i=(i + 1), text="t"))
    coord_denotes.append(coord_denote(x=end - 5, i=(i + 1), text="t'"))

print(template.format(
    lines="\n    ".join(lines),
    projections="\n      ".join(projections),
    circles="\n  ".join(circles),
    coord_denotes="\n    ".join(coord_denotes)
))
