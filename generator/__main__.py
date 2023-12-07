"""
    module entry point
"""

import sys
from dependency_injector.wiring import Provide, inject

from generator.container import Container
from generator.director.director import Director
from generator.builder.builder import Builder
from generator.render.renderer import Renderer
from generator.node.page import Page

def main(
    path:str,
    director:Director = Provide[Container.file_system_source_director],
    builder:Builder = Provide[Container.template_builder],
    renderer:Renderer = Provide[Container.renderer]
):
    """
        create the node tree from the source directory
    """
    director.set_builder(builder)
    director.make(path)

    index_page = builder.get_result()

    # debug_page_node(index_page)

    """
        generate the static web pages
    """
    root_page_html = renderer.render(index_page.get_children()[0])

    print(root_page_html)


def debug_page_node(node:Page) -> None:
    # debug
    print(node)
    for child in node.get_children():
        print(child)
        for grand_child in child.get_children():
            print(grand_child)


if __name__ == "__main__":

    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main(*sys.argv[1:])