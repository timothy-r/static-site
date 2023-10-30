"""
"""
from generator.node.page import Page

class IndexPage(Page):
    """
        Extracts the contents of an index page that are specific to that page
    """
    def get_sub_heading(self) -> str:
        return ''

    def get_thumbnail_path(self) -> str:
        return ''

    def get_contents(self) -> dict:
        return {}
