import abc

from generator.builder.builder import Builder
from generator.node.page import Page

class Director:
    """
        base class for directors
    """
    def __init__(self, builder:Builder) -> None:
        self._builder = builder

    @abc.abstractmethod
    def make(self, path:str) -> Page:
        """
            interface method to build a node tree
        """
        pass