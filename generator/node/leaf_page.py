from generator.node.page import Page

class LeafPage(Page):

    def add_child(self, child:"Page") -> None:
        raise TypeError("Cannot add a child to a LeafPage")