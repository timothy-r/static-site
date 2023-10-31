import unittest

from generator.node.leaf_page import LeafPage
from generator.node.index_page import IndexPage

class LeftPageTest(unittest.TestCase):

    def test_get_path(self) -> None:
        path = 'funky_photo.png'
        page = LeafPage(title='Funky Photo', path=path)

        self.assertEqual(path, page.get_path())

    def test_get_path_with_parent(self) -> None:
        root_page = IndexPage(title='Home Page', path='/')
        dir_page = IndexPage(title='Folder One', path='one/')
        root_page.add_child(dir_page)

        path = 'funky_photo.png'
        page = LeafPage(title='Funky Photo', path=path)
        dir_page.add_child(page)

        self.assertEqual('/one/' + path, page.get_path())

    def test_get_sibling_pages(self) -> None:
        root_page = IndexPage(title='Home Page', path='/')

        page_1 = LeafPage(title='Funky Photo', path='funky_photo.png')
        root_page.add_child(page_1)

        page_2 = LeafPage(title='Funky Photo 2', path='funky_photo_two.png')
        root_page.add_child(page_2)

        self.assertEqual(None, page_1.get_prev())
        self.assertEqual(page_2, page_1.get_next())
        self.assertEqual(page_1, page_2.get_prev())
        self.assertEqual(None, page_2.get_next())

    def test_cannot_add_child_to_leaf(self) -> None:
        page = LeafPage(title='Funky Photo', path="path")
        page_2 = LeafPage(title='Funky Photo 2', path="path_2")
        try:
            page.add_child(page_2)
        except TypeError:
            self.assertTrue(True)

        self.assertEqual(None, page.get_children())
        self.assertEqual(None, page_2.get_parent())