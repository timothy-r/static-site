from jinja2 import Environment, FileSystemLoader, select_autoescape

from generator.node.page import Page

class Renderer:
    """
        renders HTML pages for Page nodes
    """

    def __init__(self, template_dir:str) -> None:
        self._env = Environment(
            loader=FileSystemLoader(searchpath=template_dir, encoding='utf-8', followlinks=False),
            autoescape=False
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
        for child in page.get_children():
            children.append(self._get_child_data(child))

        return template.render(
            stylesheets=[],
            inline_styles= common['inline_css'],
            page_title=page.get_title(),
            albums=children,
            owner = common['owner'],
            page_js = common['inline_js'],
        )

    def _get_child_data(self, page:Page) -> dict:
        # template expects these properties
        # {
        #     'href': 'v/FX+artist+showreel/index.html',
        #     'img_src': 'd/1156-4/FX+artist+showreel.png',
        #     'img_alt': 'FX artist showreel',
        #     'img_height': '67',
        #     'img_width': '100',
        #     'title': 'FX artist showreel',
        #     'sub_title': 'FX artist showreel',
        #     'contents': '1 Image'
        # }

        return {
            'href': page.get_path(),
            'img_src': '',
            'img_alt': '',
            'img_height': '',
            'img_width': '',
            'title': page.get_title(),
            'sub_title': page.get_contents(),
            'contents': len(page.get_children()) if page.get_children() else 0
        }

    def _render_leaf_page(self, page:Page) -> None:
        """
        """
        return ''