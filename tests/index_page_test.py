# import unittest

from unittest import TestCase, mock
from generator.node.index_page import IndexPage
from generator.file.file import File

class IndexPageTest(TestCase):

    def test_get_path(self) -> None:
        root_page = IndexPage(title='Home Page', path='/')

        self.assertEqual('/', root_page.get_path())

    def test_child_dir_path(self) -> None:
        root_page = IndexPage(title='Home Page', path='/')
        dir_page = IndexPage(title='Folder One', path='one')
        root_page.add_child(dir_page)

        self.assertEqual('/one', dir_page.get_path())

    def test_child_sub_dir_path(self) -> None:
        root_page = IndexPage(title='Home Page', path='/')
        dir_page = IndexPage(title='Folder One', path='one/')
        root_page.add_child(dir_page)
        sub_dir_page = IndexPage(title='Folder Two', path='two')
        dir_page.add_child(sub_dir_page)

        self.assertEqual('/one/two', sub_dir_page.get_path())

    def test_add_child(self) -> None:
        root_page = IndexPage(title='Home Page', path='/')
        child_page = IndexPage(title='Child', path='child/')
        root_page.add_child(child=child_page)
        children = root_page.get_children()

        self.assertEqual(1, len(children))

    def test_get_sibling_pages(self) -> None:
        root_page = IndexPage(title='Home Page', path='/')
        child_page_1 = IndexPage(title='Child 1', path='child_1/')
        root_page.add_child(child=child_page_1)
        child_page_2 = IndexPage(title='Child 2', path='child_2/')
        root_page.add_child(child=child_page_2)

        self.assertEqual(child_page_1.get_next(), child_page_2)
        self.assertEqual(child_page_2.get_next(), None)

        self.assertEqual(child_page_1.get_prev(), None)
        self.assertEqual(child_page_2.get_prev(), child_page_1)

    def test_add_child_does_not_add_duplicates(self) -> None:
        """
            test that pages do not allow duplicate children
        """
        root_page = IndexPage(title='Home Page', path='/')
        child_page_1 = IndexPage(title='Child 1', path='child_1/')
        root_page.add_child(child=child_page_1)
        root_page.add_child(child=child_page_1)

        self.assertEqual(1, len(root_page.get_children()))

    def test_get_properties(self) -> None:
        """
            test getting properties from a page
        """
        inline_styles = '.content { width: 700px; }'
        root_page = IndexPage(title='Home Page', path='/', properties={'inline_styles': inline_styles})
        result = root_page.get_property('inline_styles')
        self.assertEqual(inline_styles, result)

    def test_get_thumbnail_file(self) -> None:
        """
            test adding a mock File thumbnail to a page
        """
        thumbnail_mock = mock.Mock()
        root_page = IndexPage(
            title='Home',
            path='/',
            properties={},
            files = {'thumbnail': thumbnail_mock}
        )
        result = root_page.get_file('thumbnail')
        self.assertEqual(thumbnail_mock, result)
