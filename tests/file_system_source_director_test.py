import unittest

from generator.director.file_system_source_director import FileSystemSourceDirector
from generator.builder.template_builder import TemplateBuilder
from generator.data_reader.yaml_data_reader import YamlDataReader

class FileSystemSourceDirectorTest(unittest.TestCase):

    def test_create_index_page(self) -> None:
        builder = TemplateBuilder()
        reader = YamlDataReader()
        director = FileSystemSourceDirector(reader=reader)

        director.set_builder(builder=builder)

        path = '../source/'
        result = director.make(path=path)