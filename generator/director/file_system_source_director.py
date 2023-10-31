
from generator.director.director import Director
from generator.node.page import Page
from generator.data_reader.data_reader import DataReader
class FileSystemSourceDirector(Director):
    """
        build a page tree from a local file system source
    """

    def __init__(self, reader:DataReader) -> None:
        self._data_reader = reader

    def make(self, path:str) -> Page:
        """
            path is the fs path to the root dir of the source files
            for the pages nodes this path is /
            yet they also need the actual fs path
            so that the site pages can be generated with contents
        """
        self._read_root_directory(path=path)
        # walk through child dirs

    def _read_root_directory(self, path:str) -> None:

        data = self._data_reader.read(path + "data.yml")
        root_data = {
            'title': data['index']['title']
        }
        self._builder.add_index_page(path='/', data=root_data)