"""
    module entry point
"""
from generator.generator import generate

def main(path:str):

    generate(path=path)

if __name__ == "__main__":
    path = "../templates"
    main(path)