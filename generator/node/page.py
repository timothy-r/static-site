from abc import abstractmethod

from generator.file.file import File
class Page:
    """
        base class interface for all nodes / pages
    """
    def __init__(
        self,
        title:str,
        path:str,
        properties:dict = {},
        files={str:File}
    ) -> None:
        self._parent = None
        self._next = None
        self._prev = None

        self._title = title
        self._path = path
        self._properties = properties
        self._files = files

    def set_parent(self, parent:"Page") -> None:
        self._parent = parent

    def get_parent(self) -> "Page":
        return self._parent

    @abstractmethod
    def add_child(self, child:"Page") -> None:
        pass

    @abstractmethod
    def get_children(self) -> list["Page"]:
        pass

    @abstractmethod
    def get_contents(self) -> dict:
        pass

    def set_next(self, next:"Page") -> None:
        self._next = next

    def get_next(self) -> "Page":
        return self._next

    def set_prev(self, prev:"Page") -> None:
        self._prev = prev

    def get_prev(self) -> "Page":
        return self._prev

    def get_path(self) -> str:
        """
            return the site path to this page
            all nodes have a path relative to the root node with path /
            to generate links to this page from other pages
        """
        if self._parent:
            return self._parent.get_path() + self._path
        else:
            return self._path

    def get_title(self) -> str:
        return self._title

    # @abstractmethod
    # def get_sub_heading(self) -> str:
    #     pass

    # def get_thumbnail_path(self) -> str:
    #     pass

    def get_property(self, name:str):
        return self._properties[name] if name in self._properties else None

    def get_file(self, name:str) -> File:
        return self._files[name] if name in self._files else None

    def __str__(self) -> str:
        return f"IndexPage(title={self._title}, path={self._path}, properties={self._properties}, children={len(self._children)})"