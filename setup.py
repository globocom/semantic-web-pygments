from distutils.core import setup

setup (
    name='semantic_web_pygments',
    packages=['semantic_web_pygments'],
    install_requires = ['pygments'],
    entry_points = {
        "pygments.lexers" : [
            "n3 = semantic_web_pygments:Notation3Lexer",
            "sparql = semantic_web_pygments:SparqlLexer"
        ]
    }
)
