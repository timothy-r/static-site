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

    def tearDown(self) -> None:
        super().tearDown()
        mockfs.restore_builtins()

    def test_create_index_page(self) -> None:
        """
            test creating an index page with basic data and no children
        """
        # sub_dir = 'folder_one/'
        # add the data.yml file contents
        root_data_path = self._root_path + 'data.yml'
        root_data = self._get_mock_data_file_contents()
        self._mfs.add_entries({
            # self._root_path + sub_dir : '',
            root_data_path: root_data
            })

        builder = TemplateBuilder()
        reader = YamlDataReader()
        director = FileSystemSourceDirector(reader=reader)

        director.set_builder(builder=builder)

        # dir = os.getcwd()
        # path = dir + '/source/'
        root_page = director.make(path=self._root_path)

        self.assertIsInstance(root_page, Page)
        children = root_page.get_children()
        self.assertEqual(0, len(children))

        # child_page = children[0]
        # self.assertIsInstance(child_page, Page)

    def _get_mock_data_file_contents(self) -> str:
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