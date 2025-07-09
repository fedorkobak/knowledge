"""
Visualize binary search trees as SVG.
"""
import drawsvg as draw  # type: ignore
from src.svg import draw_arrow
from typing import TypeAlias, Any


BST: TypeAlias = tuple[Any, 'BST | None', 'BST | None'] | None

NODE_RADIUS = 30
SIBLINGS_DISTANCE = 2 * NODE_RADIUS
COUSINS_DISTANCE = 2 * NODE_RADIUS
NODE_FONT_SIZE = 20
LAYERS_DISTANCE = 3 * NODE_RADIUS


def get_max_depth(tree: BST) -> int:
    """
    Calculate the maximum depth of a binary search tree.

    Parameters
    ----------
    tree : BST
        The binary search tree represented as a tuple.

    Returns
    -------
    int
        The maximum depth of the tree. 1 for only root node.
    """
    if not tree:
        return 0
    left_depth = (get_max_depth(tree[1]) if tree[1] is not None else 0)
    right_depth = (get_max_depth(tree[2]) if tree[2] is not None else 0)
    return 1 + max(left_depth, right_depth)


def get_node_svg(
    content: str, cx: float, cy: float, r: float = NODE_RADIUS
) -> draw.Group:
    """
    Create an SVG representation of a node.

    Parameters
    ----------
    content : str
        The content to display in the node.
    cx : float
        The x-coordinate of the center of the node.
    cy : float
        The y-coordinate of the center of the node.
    r : float, optional
        The radius of the node, by default NODE_RADIUS.

    Returns
    -------
    list[draw.Group]
        Group containing the SVG elements for the node.
    """
    node = draw.Circle(
        cx=cx, cy=cy, r=r, stroke='black', stroke_width=2, fill='none'
    )
    text = draw.Text(
        content,
        x=cx, y=cy,
        font_size=NODE_FONT_SIZE,
        text_anchor='middle',
        dominant_baseline='middle',
        fill='black'
    )
    group = draw.Group([node, text])
    return group


def get_arrow(
    x1: float, y1: float,
    x2: float, y2: float,
    radius: float = NODE_RADIUS
) -> draw.Path:
    """
    Draw an arrow from one node to another. You only need to specify the
    centers of the nodes.

    Parameters
    ----------
    x1: float
        The x-coordinate of the start node.
    y1: float
        The y-coordinate of the start node.
    x2: float
        The x-coordinate of the end node.
    y2: float
        The y-coordinate of the end node.
    """
    dx = (x2 - x1)
    dy = (y2 - y1)

    length = (dx**2 + dy**2)**0.5

    dx /= length
    dy /= length

    x1 = x1 + dx * radius
    y1 = y1 + dy * radius
    x2 = x2 - dx * radius
    y2 = y2 - dy * radius

    return draw_arrow(
        sx=x1, sy=y1,
        ex=x2, ey=y2,
        color='black'
    )


def count_width(depth: int) -> float:
    """
    Calculate the width of the tree at a given depth.

    Parameters
    ----------
    depth : int
        The depth of the tree.

    Returns
    -------
    float
        The width of the tree at the specified depth.
    """
    max_leaf_nubmer = 2 ** (depth - 1)
    return (
        (max_leaf_nubmer / 2) * SIBLINGS_DISTANCE +
        ((max_leaf_nubmer / 2) - 1) * COUSINS_DISTANCE +
        max_leaf_nubmer * NODE_RADIUS * 2
    )


def tree_to_svg(
    tree: BST,
    shift_x: float = 0,
    shift_y: float = 0,
    depth: int | None = None,
    accumulated_elements: list[draw.DrawingElement] | None = None
) -> list[draw.DrawingElement]:
    """
    Recurrently convert a binary search tree to an svgdraw components.

    Parameters
    ----------
    tree : BST
        The binary search tree represented as a tuple.
    shift_x : float, optional
        Horizontal shift for the drawing, by default 0.
    shift_y : float, optional
        Vertical shift for the drawing, by default 0.
    depth : int, optional
        The depth of the tree to visualize. Supposed to be calculated at first
        step of the recurrent procedure.
    accumulated_elements : list[draw.DrawingElement], optional
        List to which to add the SVG elements, contains elements added at the
        previous steps.

    Returns
    -------
    list[draw.DrawingElement]
        A list of SVG drawing elements representing the tree.
    """
    if accumulated_elements is None:
        accumulated_elements = []
    if depth is None:
        depth = get_max_depth(tree)

    if tree is None:
        return accumulated_elements

    width = count_width(depth)
    cx = width / 2 + shift_x
    cy = shift_y + NODE_RADIUS

    accumulated_elements.append(get_node_svg(
        content=str(tree[0]),
        cx=cx, cy=cy,
        r=NODE_RADIUS,
    ))

    # Note: nested trees doesn't count distances between cousins during width
    # count as they belongs to the other tree.
    if tree[1] is not None:
        tree_to_svg(
            tree=tree[1],
            shift_x=shift_x,
            shift_y=shift_y + LAYERS_DISTANCE,
            depth=depth - 1,
            accumulated_elements=accumulated_elements
        )
        accumulated_elements.append(get_arrow(
            x1=cx, y1=cy,
            x2=shift_x + (width - COUSINS_DISTANCE) / 4,
            y2=shift_y + LAYERS_DISTANCE + NODE_RADIUS
        ))
    if tree[2] is not None:
        tree_to_svg(
            tree=tree[2],
            shift_x=shift_x + width / 2 + COUSINS_DISTANCE / 2,
            shift_y=shift_y + LAYERS_DISTANCE,
            depth=depth - 1,
            accumulated_elements=accumulated_elements
        )
        accumulated_elements.append(get_arrow(
            x1=cx, y1=cy,
            x2=shift_x + (width / 2 + COUSINS_DISTANCE / 2) / 2 + width / 2,
            y2=shift_y + LAYERS_DISTANCE + NODE_RADIUS
        ))
    return accumulated_elements


def visualize_tree(tree: BST) -> draw.Drawing:
    """
    Get svgdraw object representing the binary search tree.

    Parameters
    ----------
    tree : BST
        The binary search tree represented as a tuple.

    Returns
    -------
    draw.Drawing
        An SVG drawing object containing the tree visualization.
    """
    depth = get_max_depth(tree)
    d = draw.Drawing(
        width=count_width(depth=depth),
        height=(depth - 1) * LAYERS_DISTANCE + 2 * NODE_RADIUS
    )
    elements = tree_to_svg(tree=tree)
    for element in elements:
        d.append(element)  # type: ignore
    return d
