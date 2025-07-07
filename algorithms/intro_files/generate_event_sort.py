from pathlib import Path
from typing import Callable
template = (Path("intro_files")/"event_sort_template").read_text()

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


def generate_coordinate_system(end: int) -> str:
    """
    Generate an SVG for the coordinate system. The X-axis extends to the
    specified point.

    Parameters
    ----------
    end: int
        Coordinate where axis ends.

    Returns
    -------
    Piece of code for axis.
    """
    return f"""
    <line x1=0 y1=150 x2={end} y2=150 />
    <line x1={end} y1=150 x2={end * 0.95} y2=160 />
    <line x1={end} y1=150 x2={end * 0.95} y2=140 />
    """.strip()


def get_visualisation(coordinates: list[tuple[int, int]]) -> str:
    """
    For given set of intervals get SVG visualisation.

    Parameters
    ----------
    coordinates: list[tuple[int, int]]
        Pairs of numbers representing the start and the end of intervals.

    Returns
    -------
    str SVG code.
    """
    coord_denotes: list[str] = []
    y_postions = [(130, 0),]
    coordinates.sort()

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
        coord_denotes.append(coord_denote(begin - 5, (i + 1), "t"))
        coord_denotes.append(coord_denote(end - 5, (i + 1), "t'"))

    axis = generate_coordinate_system(int(coordinates[-1][1] * 1.1))

    return template.format(
        lines="\n    ".join(lines),
        projections="\n      ".join(projections),
        circles="\n  ".join(circles),
        coord_denotes="\n    ".join(coord_denotes),
        axis=axis
    )
