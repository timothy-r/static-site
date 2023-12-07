import abc

class File:
    """
        represent a file to be embedded into page
        eg.
        source = /Users/user_name/Documents/Code/static-site/source/folder_one/image.png
        site_path = /folder_one/image.png
    """
    def __init__(self, source:str, site_path:str) -> None:
        """
            set the source of the file
            implementations use this for a local fs page, an S3 object, a HTTP resource etc
        """
        self._source = source
        self._site_path = site_path

    def get_source(self) -> str:
        """
            access the source location string
        """
        return self._source

    def get_site_path(self) -> str:
        """
            access the location of this file on the generated site
        """
        return self._site_path

    @abc.abstractmethod
    def copy_to_local_fs(self, target:str) -> bool:
        """
            copy the source file to the local fs path
        """
        pass