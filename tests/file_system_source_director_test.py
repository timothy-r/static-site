import unittest
import mockfs

from generator.director.file_system_source_director import FileSystemSourceDirector
from generator.builder.template_builder import TemplateBuilder
from generator.data_reader.yaml_data_reader import YamlDataReader
from generator.node.page import Page
class FileSystemSourceDirectorTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._mfs = mockfs.replace_builtins()
        self._root_path = '/Users/test/source/'
        self._mfs.add_entries({self._root_path : ''})

        builder = TemplateBuilder()
        reader = YamlDataReader()
        self._director = FileSystemSourceDirector(reader=reader)

        self._director.set_builder(builder=builder)

    def tearDown(self) -> None:
        super().tearDown()
        mockfs.restore_builtins()

    def test_create_index_page(self) -> None:
        """
            test creating an index page with basic data and no children
        """
        self._add_mock_root_directory()

        root_page = self._director.make(path=self._root_path)

        self.assertIsInstance(root_page, Page)
        children = root_page.get_children()
        self.assertEqual(0, len(children))

    def test_create_sub_dirs(self) -> None:
        self._add_mock_root_directory()
        # create sub dirs with data files
        self._add_mock_directory('folder_one')
        self._add_mock_directory('folder_one/sub_dir_one')
        self._add_mock_directory('folder_two')
        self._add_mock_directory('folder_two/sub_dir_two')

        root_page = self._director.make(path=self._root_path)

        self.assertIsInstance(root_page, Page)
        children = root_page.get_children()
        self.assertEqual(2, len(children))
        for child in children:
            self.assertIsInstance(child, Page)
            grand_children = child.get_children()
            self.assertEqual(1, len(grand_children))
            self.assertIsInstance(grand_children[0], Page)

    def test_create_leaf_page(self) -> None:
        self._add_mock_root_directory()
        # create sub dirs with data files
        self._add_mock_directory('folder_one')
        self._add_mock_file('folder_one/funky.png')
        self._add_mock_file('folder_one/blog_post.txt')
        self._add_mock_file('folder_one/cool_video.mp4')

        root_page = self._director.make(path=self._root_path)
        children = root_page.get_children()
        self.assertEqual(1, len(children))
        grand_children = children[0].get_children()
        self.assertEqual(3, len(grand_children))
        for grand_child in grand_children:
            self.assertIsInstance(grand_child, Page)


    def _add_mock_file(self, path:str) -> None:
        full_path = self._root_path + path
        self._mfs.add_entries({
            full_path: ''
        })

    def _add_mock_directory(self, path:str) -> None:
        data_path = self._root_path + path + '/data.yml'
        data = self._get_test_data_file_contents()
        self._mfs.add_entries({
            data_path: data
        })

    def _add_mock_root_directory(self) -> None:
        # add the data.yml file contents
        root_data_path = self._root_path + 'data.yml'
        root_data = self._get_test_root_data_file_contents()
        self._mfs.add_entries({
            root_data_path: root_data
            })

    def _get_test_root_data_file_contents(self) -> str:
        return """
index:
    title: "My site"
common:
    owner:
        name: "My site owner"
        email: "My email"
    css:
        inline: css/inline_styles.css
    js:
        inline: js/inline_scripts.js
    """

    def _get_test_data_file_contents(self) -> str:
        return """
index:
    title: "Folder One"
    thumb: "thumb.png"
    sub_heading: "Folder one is the best folder"
contents:
    funky_foto:
      type: "img"
      title: "Funky Foto"
      src: "funky.png"
      height: 576
      width: 1024
    blog_post:
      type: "txt"
      title: "Blog Post"
      src: "blog_post.txt"
    cool_vid:
      type: "video"
      title: "Cool Video"
      src: "cool_video.mp4"
"""