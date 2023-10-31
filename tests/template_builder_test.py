import unittest

from generator.builder.template_builder import TemplateBuilder
from generator.node.page import Page
from generator.node.index_page import IndexPage

class TemplateBuilderTest(unittest.TestCase):

    def test_create_index_page(self):
        builder = TemplateBuilder()
        builder.add_index_page('/', {'title': 'Home page'})

        result = builder.get_result()
        self.assertIsInstance(result, IndexPage)

    def test_create_child_index_pages(self):
        builder = TemplateBuilder()
        builder.add_index_page('/', {'title': 'Home page'})
        builder.add_index_page('child/', {'title': 'Child'})
        builder.add_index_page('grand_child_a/', {'title': 'Grand Child A'})
        builder.set_current_directory('/child/')
        builder.add_index_page('grand_child_b/', {'title': 'Grand Child B'})

        root = builder.get_result()
        self.assertIsInstance(root, IndexPage)

        self.assertEquals(len(root.get_children()), 1)
        children = root.get_children()

        child = children[0]

        self.assertIsInstance(child, IndexPage)
        grand_children = child.get_children()
        self.assertEquals(len(grand_children), 2)

    def test_reset_clears_builder_state(self) -> None:
        builder = TemplateBuilder()
        builder.add_index_page('/', {'title': 'Home page'})
        builder.reset()

        node = builder.get_result()
        self.assertIsNone(node)