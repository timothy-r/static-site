from generator.node.page import Page

class LeafPage(Page):

    def add_child(self, child:"Page") -> None:
        raise TypeError("Cannot add a child to a LeafPage")

    def get_children(self) -> list["Page"]:
        return None

    def is_leaf_page(self) -> bool:
        return True
