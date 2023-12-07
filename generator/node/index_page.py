"""
"""
from generator.node.page import Page
from generator.file.file import File

class IndexPage(Page):
    """
        Extracts the contents of an index page that are specific to that page
    """
    def __init__(
        self,
        title: str,
        path: str,
        properties:dict = {},
        files={str:File}
    ) -> None:
        super().__init__(title, path, properties=properties, files=files)
        self._children = []

    def get_sub_heading(self) -> str:
        return ''

    def add_child(self, child: Page) -> None:
        """
            adds a child page, sets the child's parent page
            sets next & prev pages on the child
        """
        if child in self._children:
            return

        if len(self._children) > 0:
            prev = self._children[-1]
            prev.set_next(next=child)
        else:
            prev = None

        self._children.append(child)

        child.set_parent(self)

        if prev:
            child.set_prev(prev=prev)

    def get_children(self) -> list["Page"]:
        return self._children

    # def __str__(self) -> str:
    #     return f"IndexPage(title={self._title}, path={self._path}, properties={self._properties}, children={len(self._children)})"