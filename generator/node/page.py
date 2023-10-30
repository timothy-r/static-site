from abc import abstractmethod

class Page:
    """
        base class interface for all nodes / pages
    """
    def __init__(self, parent:"Page", title:str, path:str) -> None:
        self._parent = parent
        self._title = title
        self._path = path

    def get_parent(self) -> "Page":
        return self._parent

    def get_children(self) -> list["Page"]:
        pass

    def get_next(self) -> "Page":
        pass

    def get_prev(self) -> "Page":
        pass

    def get_path(self) -> str:
        """
            return the path to this page
            to store the file
            to generate links to this page from other pages
        """
        if self._parent:
            return self._parent.get_path() + self._path
        else:
            return self._path

    @abstractmethod
    def get_title(self) -> str:
        return self._title

    @abstractmethod
    def get_sub_heading(self) -> str:
        pass

    @abstractmethod
    def get_thumbnail_path(self) -> str:
        pass