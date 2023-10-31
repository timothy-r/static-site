"""
    module entry point
"""
from generator.generator import generate

def main(path:str):

    page = generate(path=path)

    print(page)

if __name__ == "__main__":
    path = "../templates"
    main(path)
