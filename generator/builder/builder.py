import abc

from generator.node.page import Page

class Builder:
    """
        interface for builder classes
    """
    @abc.abstractmethod
    def add_index_page(self, path:str, data:dict) -> None:
        pass

    @abc.abstractmethod
    def add_text_page(self, path:str, data:dict, full_path:str) -> None:
        """
            adds a page with just text contents (within a html document)
        """
        pass

    @abc.abstractmethod
    def add_image_page(self, path:str, data:dict, full_path:str) -> None:
        pass

    @abc.abstractmethod
    def add_video_page(self, path:str, data:dict, full_path:str) -> None:
        pass

    @abc.abstractmethod
    def get_result(self) -> Page:
        """
            returns the root page node in the tree
        """
        pass

    @abc.abstractmethod
    def get_current_directory(self) -> str:
        """
            return the path of the current node
        """
        pass

    @abc.abstractmethod
    def set_current_directory(self, full_path:str) -> bool:
        pass

    @abc.abstractmethod
    def reset(self) -> None:
        pass
