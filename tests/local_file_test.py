from unittest import TestCase
import os

from generator.file.local_file import LocalFile

class LocalFileTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._test_file = os.path.dirname(__file__) + "/fixtures/digitalis02.jpg"
        self._test_target_file = os.path.dirname(__file__) + "/fixtures/test_file.jpg"
        if os.path.isfile(self._test_target_file):
            os.remove(self._test_target_file)

    def tearDown(self) -> None:
        super().tearDown()
        # remove copied files
        if os.path.isfile(self._test_target_file):
            os.remove(self._test_target_file)

    def test_copy(self) -> None:
        file = LocalFile(source=self._test_file, site_path='/index.png')
        result = file.copy_to_local_fs(self._test_target_file)
        self.assertTrue(result)
        self.assertTrue(os.path.isfile(self._test_target_file))