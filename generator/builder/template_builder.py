from generator.builder.builder import Builder
from generator.node.page import Page
from generator.node.leaf_page import LeafPage
from generator.node.index_page import IndexPage

class TemplateBuilder(Builder):

    def __init__(self) -> None:
        super().__init__()
        self.reset()

    def add_index_page(self, path: str, data: dict) -> None:
        node = IndexPage(data['title'], path)
        if self._current_node:
            self._current_node.add_child(node)

        full_path = node.get_path()
        self._node_index[full_path] = node
        self._current_node = node

    def add_text_page(self, path: str, data: dict) -> None:
        pass

    def add_image_page(self, path: str, data: dict) -> None:
        pass

    def add_video_page(self, path: str, data: dict) -> None:
        pass

    def get_result(self) -> Page:
        return self._get_root_node()

    def reset(self) -> None:
        self._current_node = None
        self._node_index = {}

    def set_current_directory(self, full_path: str) -> bool:
        """
            allow clients to change the current dir
            using the full path to the target dir node
        """
        if full_path in self._node_index:
            self._current_node = self._node_index[full_path]
            return True
        else:
            return False

    def _get_root_node(self) -> Page:
        """
            look up the root node from the current node
        """
        node = self._current_node

        while node:
            parent = node.get_parent()
            if not parent:
                return node
            else:
                node = parent

        return None