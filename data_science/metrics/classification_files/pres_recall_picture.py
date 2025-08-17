import random
import pyperclip
import drawsvg as dw


random.seed(5)
scatter_radius = 10
FN_color = "#90DE99"
TN_color = "#DE9090"
TP_color = "#44DB54"
FP_color = "#DB4444"

drawing = dw.Drawing(800, 600)

drawing.append(dw.Rectangle(0, 0, 250, 500, fill=FN_color))
drawing.append(dw.Rectangle(250, 0, 250, 500, fill=TN_color))

drawing.append(dw.Path(
    d="M 250 100 A 150 150 0 0 0 250 400",
    stroke="black",
    stroke_width=5,
    fill=TP_color
))
drawing.append(dw.Path(
    d="M 250 100 A 150 150 0 0 1 250 400",
    stroke="black",
    stroke_width=5,
    fill=FP_color
))

# Draw scatter
positive = [
    (random.randint(5, 245), random.randint(5, 495))
    for _ in range(10)
]
negative = [
    (random.randint(255, 495), random.randint(5, 495))
    for i in range(10)
]

scatter = dw.Group(stroke="Gray")

for x, y in positive:
    scatter.append(dw.Circle(x, y, scatter_radius, fill="Gray"))

for x, y in negative:
    circle = dw.Circle(
        x, y, scatter_radius,
        fill="None",
        stroke="Gray",
        stroke_width=5,
    )
    scatter.append(circle)
drawing.append(scatter)

texts = dw.Group(
    dominant_baseline="middle",
    color="black"
)
font_size = 23
texts.append(dw.Text(
    text="false negatives",
    font_size=font_size,
    x=40, y=20
))
texts.append(dw.Text(
    text="true negatives",
    font_size=font_size,
    x=300, y=20
))
texts.append(dw.Text(
    text="false positives",
    font_size=font_size,
    x=250, y=250
))
texts.append(dw.Text(
    text="true positives",
    font_size=font_size,
    x=105, y=250
))
drawing.append(texts)

# Precision formula
drawing.append(dw.Text(
    "Precision =",
    x=520, y=110,
    dominant_baseline="middle",
    font_size=font_size
))
drawing.append(dw.Path(
    d="M 715 0 A 50 50 0 0 0 715 100",
    fill=TP_color
))
drawing.append(dw.Path(
    d="M 700 120 A 50 50 0 0 0 700 220",
    fill=TP_color
))
drawing.append(dw.Path(
    d="M 700 120 A 50 50 0 0 1 700 220",
    fill=FP_color
))
drawing.append(dw.Line(650, 110, 750, 110, stroke="black"))

# Recall formula
drawing.append(dw.Text(
    "Recall =",
    x=520, y=360,
    dominant_baseline="middle",
    font_size=font_size
))
drawing.append(dw.Path(
    d="M 715 250 A 50 50 0 0 0 715 350",
    fill=TP_color
))
drawing.append(dw.Rectangle(
    655, 370, 90, 170,
    fill=FN_color
))
drawing.append(dw.Path(
    d="M 745 405 A 50 50 0 0 0 745 505",
    fill=TP_color
))
drawing.append(dw.Line(650, 360, 750, 360, stroke="black"))

svg_code = drawing.as_svg()
if svg_code is not None:
    pyperclip.copy(svg_code)
