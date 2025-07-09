"""
Tools that extend drawsvg to add really typical shapes and symbols.
"""
import drawsvg as draw


def draw_arrow(
    sx: int, sy: int,
    ex: int, ey: int,
    width: int = 3,
    arrow_head_width: int = 10,
    color: str = 'black'
) -> draw.Path:
    """
    Draw an arrow from (sx, sy) to (ex, ey).

    Parameters
    ----------
    sx: int, sy: int,
        Start coordinates of the arrow.
    ex: int, ey: int,
        End coordinates of the arrow.
    width: int = 3,
        Width of the arrow line.
    arrow_head_width: int = 10,
        Width of the arrowhead.
    color: str = 'black'
        Color of the arrow.

    Returns
    -------
    draw.Path
        A Path object representing the arrow.
    """
    dx = ex - sx
    dy = ey - sy
    length = (dx**2 + dy**2)**0.5

    # Normalize direction
    dx /= length
    dy /= length

    # Perpendicular vector for arrowhead
    perp_dx = -dy * arrow_head_width / 2
    perp_dy = dx * arrow_head_width / 2

    # Arrowhead points
    p1x = ex - dx * arrow_head_width + perp_dx
    p1y = ey - dy * arrow_head_width + perp_dy
    p2x = ex - dx * arrow_head_width - perp_dx
    p2y = ey - dy * arrow_head_width - perp_dy

    path = draw.Path(fill=color, stroke=color, stroke_width=width)
    path.M(sx, sy)
    path.L(ex, ey)
    path.M(ex, ey)
    path.L(p1x, p1y)
    path.L(p2x, p2y)
    return path
