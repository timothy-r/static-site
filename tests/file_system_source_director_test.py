import unittest
import os

from generator.director.file_system_source_director import FileSystemSourceDirector
from generator.builder.template_builder import TemplateBuilder
from generator.data_reader.yaml_data_reader import YamlDataReader
from generator.node.page import Page
class FileSystemSourceDirectorTest(unittest.TestCase):

    def test_create_index_page(self) -> None:
        builder = TemplateBuilder()
        reader = YamlDataReader()
        director = FileSystemSourceDirector(reader=reader)

        director.set_builder(builder=builder)

        dir = os.getcwd()
        path = dir + '/source/'
        result = director.make(path=path)

        self.assertIsInstance(result, Page)