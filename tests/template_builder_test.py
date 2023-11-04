import unittest

from generator.builder.template_builder import TemplateBuilder
from generator.node.page import Page
from generator.node.index_page import IndexPage

class TemplateBuilderTest(unittest.TestCase):

    def setUp(self) -> None:

        super().setUp()
        self._builder = TemplateBuilder()

    def test_create_index_page(self):
        self._builder.add_index_page('/', {'title': 'Home page'})

        result = self._builder.get_result()
        self.assertIsInstance(result, IndexPage)

    def test_create_child_index_pages(self):
        self._builder.add_index_page('/', {'title': 'Home page'})
        self._builder.add_index_page('child/', {'title': 'Child'})
        current_path = self._builder.get_current_directory()

        self._builder.add_index_page('grand_child_a/', {'title': 'Grand Child A'})
        self._builder.set_current_directory(current_path)
        self._builder.add_index_page('grand_child_b/', {'title': 'Grand Child B'})

        root = self._builder.get_result()
        self.assertIsInstance(root, IndexPage)

        self.assertEqual(len(root.get_children()), 1)
        children = root.get_children()

        child = children[0]

        self.assertIsInstance(child, IndexPage)
        grand_children = child.get_children()
        self.assertEqual(len(grand_children), 2)

    def test_reset_clears_builder_state(self) -> None:
        self._builder.add_index_page('/', {'title': 'Home page'})
        self._builder.reset()

        node = self._builder.get_result()
        self.assertIsNone(node)

    def test_builder_adds_template_vars(self) -> None:
        template_vars = {'key': 'value'}
        self._builder.add_index_page('/', {'title': 'Home page'})