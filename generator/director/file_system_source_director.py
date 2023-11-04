import os

from generator.director.director import Director
from generator.node.page import Page
from generator.data_reader.data_reader import DataReader
class FileSystemSourceDirector(Director):
    """
        build a page tree from a local file system source
    """

    def __init__(self, reader:DataReader) -> None:
        """
            initialise instance variables
        """
        self._data_reader = reader
        self._common_data = {}

    def make(self, path:str) -> Page:
        """
            path is the fs path to the root dir of the source files
            for the pages nodes this path is /
            yet they also need the actual fs path
            so that the site pages can be generated with contents
        """
        self._read_common_data(full_path=path)

        self._read_sub_directory(full_path=path, dir_name='/')

        # return the result
        return self._builder.get_result()

    # def _read_root_directory(self, full_path:str) -> None:
    #     """
    #         read the root directory node
    #         read the common data for all page nodes
    #     """
    #     data = self._data_reader.read(full_path + "data.yml")
    #     node_data = {
    #         'title': data['index']['title'],
    #         'local_path': full_path
    #     }
    #     self._builder.add_index_page(path='/', data=node_data)

    def _read_common_data(self, full_path:str) -> None:
        """
            from the root directory read all the data common to all pages
            including paths to css & js files
        """

    def _read_sub_directory(self, full_path:str, dir_name:str) -> str:
        """
            read a directory into a node
            full_path is the fs path, use the last dir name for the node 'site path'
        """
        yml_file = full_path + "/data.yml"
        if not os.path.isfile(yml_file):
            return

        data = self._data_reader.read(yml_file)

        # merge common data into the node data
        node_data = data['index']
        contents_data = data['contents'] if 'contents' in data else {}

        node_data['local_path'] = full_path

        """
            add a node for this directory
        """
        self._builder.add_index_page(path=dir_name, data=node_data)

        # for each child dir add a child node
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            if os.path.isdir(item_path):

                current_path = self._builder.get_current_directory()
                dir_name = item + '/'
                self._read_sub_directory(full_path=item_path, dir_name=dir_name)
                # reset builder dir to this dir
                self._builder.set_current_directory(current_path)

            elif os.path.isfile(item_path):
                # look for this item_path in the yaml data
                # if it's present then add a leaf node
                self._read_leaf_page(item_path, contents_data)

    def _read_leaf_page(self, item_path:str, contents_data:dict) -> None:
        """
            add a leaf page to the tree,
            if specified in the data for the directory
        """
        # extract filename from path
        file_name = os.path.basename(item_path)

        for item in contents_data.values():
            if item['src'] and item['src'] == file_name:
                type = item['type']
                if 'img' == type:
                    self._builder.add_image_page(path=file_name, data=item, full_path=item_path)
                elif 'txt' == type:
                    self._builder.add_text_page(path=file_name, data=item, full_path=item_path)
                elif 'video' == type:
                    self._builder.add_video_page(path=file_name, data=item, full_path=item_path)
                break
