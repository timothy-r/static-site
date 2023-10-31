
from generator.director.director import Director
from generator.node.page import Page

class FileSystemSourceDirector(Director):
    """
        build a page tree from a local file system source
    """
    def make(self, path: str) -> Page:
        """
            path is the fs path to the root dir of the source files
        """
        pass
