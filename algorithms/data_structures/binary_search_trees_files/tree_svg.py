"""
Visualize binary search trees as SVG.
"""
import drawsvg as draw  # type: ignore
# from src.svg import draw_arrow
from typing import TypeAlias, Any


BST: TypeAlias = tuple[Any, 'BST | None', 'BST | None'] | None

NODE_RADIUS = 20
SIBLINGS_DISTANCE = 4 * NODE_RADIUS
COUSINS_DISTANCE = 2 * NODE_RADIUS


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


def tree_to_svg(
    tree: BST,
    shift_x: float = 0,
    shift_y: float = 0,
    depth: int | None = None,
    accumulated_elements: list[draw.DrawingElement] = []
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
    if depth is None:
        depth = get_max_depth(tree)
    max_leaf_nubmer = 2 ** (depth - 1)

    if tree is None:
        return accumulated_elements

    width = (
        (max_leaf_nubmer / 2) * SIBLINGS_DISTANCE +
        (max_leaf_nubmer / 2) * COUSINS_DISTANCE +
        max_leaf_nubmer * NODE_RADIUS * 2
    )

    accumulated_elements.append(draw.Circle(
        cx=width / 2 + shift_x,
        cy=shift_y + NODE_RADIUS,
        r=NODE_RADIUS,
        stroke='black',
        stroke_width=2
    ))

    tree_to_svg(
        tree=tree[1],
        shift_x=shift_x,
        shift_y=shift_y + NODE_RADIUS * 4,
        depth=depth - 1,
        accumulated_elements=accumulated_elements
    )
    tree_to_svg(
        tree=tree[2],
        shift_x=shift_x + width / 2,
        shift_y=shift_y + NODE_RADIUS * 4,
        depth=depth - 1,
        accumulated_elements=accumulated_elements
    )
    return accumulated_elements


def visualize_tree(tree: BST) -> draw.Drawing:
    depth = get_max_depth(tree)
    max_leaf_nubmer = 2 ** (depth - 1)
    distances_between_siblings = 4 * NODE_RADIUS
    distances_between_cousins = 2 * NODE_RADIUS
    width = (
        (max_leaf_nubmer / 2) * distances_between_siblings +
        (max_leaf_nubmer / 2) * distances_between_cousins
    )
    height = depth * (NODE_RADIUS * 4)

    d = draw.Drawing(width=width, height=height)
    current_level = [tree]
    for i in range(depth):

        new_level: list[BST] = []
        for j, node in enumerate(current_level):

            x = width * (j + 1) / (i + 2)
            d.append(  # type: ignore
                draw.Circle(
                    cx=x, cy=(i * NODE_RADIUS * 4) + NODE_RADIUS,
                    r=NODE_RADIUS, stroke='black'
                )
            )

            if node is not None:
                new_level.append(node[1])
                new_level.append(node[2])
            else:
                new_level.append(None)
                new_level.append(None)

        current_level = new_level

    return d
