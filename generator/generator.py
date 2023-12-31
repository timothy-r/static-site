from jinja2 import Environment, PackageLoader, select_autoescape

def generate(path:str):
    env = Environment(
        loader=PackageLoader(package_name="generator", package_path=path, encoding='utf-8'),
        autoescape=select_autoescape()
    )

    template = env.get_template("index.html")

    # common
    stylesheets = [
        {'href':'modules/icons/iconpacks/silk/icons.css'},
        {'href':'themes/noodle/theme.css'}
    ]

    # common
    inline_styles = """.content { width: 700px; }
    .gallery-thumb { width: 130px; height: 130px; }"""

    # page specific
    title='Kayu-FX'

    # page specific
    albums = [
        {
            'href': 'v/FX+artist+showreel/index.html',
            'img_src': 'd/1156-4/FX+artist+showreel.png',
            'img_alt': 'FX artist showreel',
            'img_height': '67',
            'img_width': '100',
            'title': 'FX artist showreel',
            'sub_title': 'FX artist showreel',
            'contents': '1 Image'
        }

    ]

    # common
    owner = {
        'email': 'mailto:flo.richer@googlemail.com',
        'name': 'Florence Richer'
    }

    # common
    page_js = """var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-27528169-1']);
        _gaq.push(['_trackPageview']);
        (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();"""

    return template.render(
        stylesheets=stylesheets,
        inline_styles= inline_styles,
        page_title=title,
        albums=albums,
        owner = owner,
        page_js = page_js
    )