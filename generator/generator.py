from jinja2 import Environment, PackageLoader, select_autoescape

def generate(path:str):
    env = Environment(
        loader=PackageLoader(package_name="generator", package_path=path, encoding='utf-8'),
        autoescape=select_autoescape()
    )

    template = env.get_template("index.html")


    print(template.render(the="variables", go="here"))