import yaml

from generator.data_reader.data_reader import DataReader

class YamlDataReader(DataReader):

    def read(self, path:str) -> dict:
        """
            read yaml file at path
        """
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
            return data