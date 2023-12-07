import shutil

from generator.file.file import File

class LocalFile(File):
    """
        represents a file on the local file system
    """
    def copy_to_local_fs(self, target:str) -> bool:
        """
            copy the source file to the local fs target path
        """
        shutil.copyfile(self._source, target)
        return True