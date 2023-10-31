"""
    module entry point
"""
from generator.generator import generate

def main(path:str):
    """
        run the test generator
    """
    page = generate(path=path)

    print(page)

if __name__ == "__main__":
    p = "../templates"
    main(p)
