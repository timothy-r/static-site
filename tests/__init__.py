"""
    test module
"""
import unittest

from tests.index_page_test import IndexPageTest
from tests.leaf_page_test import LeftPageTest
from tests.template_builder_test import TemplateBuilderTest
from tests.file_system_source_director_test import FileSystemSourceDirectorTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()

    runner.run(suite)
