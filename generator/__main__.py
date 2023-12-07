"""
    module entry point
"""

import sys
from dependency_injector.wiring import Provide, inject

from generator.container import Container
from generator.director.director import Director
from generator.builder.builder import Builder

def main(
    path:str,
    director:Director = Provide[Container.file_system_source_director],
    builder:Builder = Provide(Container.template_builder)
):
    """
        create the node tree from the source directory
    """
    director.set_builder(builder)
    director.make(path)

    index_page = builder.get_result()

    # debug
    print(index_page)
    for child in index_page.get_children():
        print(child)
        for grand_child in child.get_children():
            print(grand_child)

    """
        generate the static web pages
    """

if __name__ == "__main__":

    container = Container()
    container.init_resources()

    container.wire(modules=[__name__])

    main(*sys.argv[1:])


# if __name__ == "__main__":
#     p = "../templates"
#     main(p)
