from dependency_injector import containers, providers

from generator.director.file_system_source_director import FileSystemSourceDirector
from generator.builder.template_builder import TemplateBuilder
from generator.data_reader.yaml_data_reader import YamlDataReader

class Container(containers.DeclarativeContainer):

    # config = providers.Configuration(yaml_files=["./config.yml"])

    yaml_data_reader = providers.Factory(
        YamlDataReader
    )

    template_builder = providers.Singleton(
        TemplateBuilder
    )

    file_system_source_director = providers.Factory(
        FileSystemSourceDirector,
        reader=yaml_data_reader
    )

