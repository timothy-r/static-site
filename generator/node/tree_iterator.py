from generator.node.page import Page

class TreeIterator:
    """
        Allows clients to iterate over a node tree
    """
    def __init__(self, root:Page) -> None:
        self._root = root
