import unittest

from generator.node.index_page import IndexPage

class IndexPageTest(unittest.TestCase):

    def test_get_path(self) -> None:
        root_page = IndexPage(parent=None, title='Home Page', path='/')

        self.assertEquals('/', root_page.get_path())

    def test_child_dir_path(self) -> None:
        root_page = IndexPage(parent=None, title='Home Page', path='/')
        dir_page = IndexPage(parent=root_page, title='Folder One', path='one')

        self.assertEquals('/one', dir_page.get_path())

    def test_child_sub_dir_path(self) -> None:
        root_page = IndexPage(parent=None, title='Home Page', path='/')
        dir_page = IndexPage(parent=root_page, title='Folder One', path='one/')
        sub_dir_page = IndexPage(parent=dir_page, title='Folder Two', path='two')

        self.assertEquals('/one/two', sub_dir_page.get_path())