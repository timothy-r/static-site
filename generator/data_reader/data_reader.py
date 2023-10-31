import abc

class DataReader():
    """
        interface for reading data
    """
    @abc.abstractmethod
    def read(self, path) -> dict:
        """
            read data from path into a dict
        """
        pass