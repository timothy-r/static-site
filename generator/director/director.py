import abc

from generator.builder.builder import Builder
from generator.node.page import Page

class Director:
    """
        base class for directors
    """

    def set_builder(self, builder:Builder) -> None:
        """
            sets or resets the builder instance
        """
        self._builder = builder

    @abc.abstractmethod
    def make(self, path:str) -> Page:
        """
            interface method to build a node tree
        """
        pass