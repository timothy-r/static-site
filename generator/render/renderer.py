from jinja2 import Environment, FileSystemLoader, select_autoescape

from generator.node.page import Page

class Renderer:
    """
        renders HTML pages for Page nodes
    """

    def __init__(self, template_dir:str) -> None:
        self._env = Environment(
            loader=FileSystemLoader(searchpath=template_dir, encoding='utf-8', followlinks=False),
            autoescape=select_autoescape()
        )
        self._index_template = 'index.html'

    def render(self, page:Page) -> None:
        """
            render the HTML page for using a template and the page's properties
        """
        if page.is_leaf_page():
            return self._render_leaf_page(page=page)
        else:
            return self._render_index_page(page=page)

    def _render_index_page(self, page:Page) -> None:
        """
        """
        template = self._env.get_template(self._index_template)
        common = page.get_property('common')
        # generate the list of child albums (directories)
        children = []
        # for child in page.get_children():

        return template.render(
            stylesheets=[],
            inline_styles= common['css']['inline'],
            page_title=page.get_title(),
            albums=children,
            owner = common['owner'],
            page_js = common['js']['inline'],
        )

    def _render_leaf_page(self, page:Page) -> None:
        """
        """
        return ''