from setuptools import setup, find_packages

setup (
    name='semantic_web_pygments',
    packages=find_packages(),
    entry_points = """
[pygments.lexer]
n3  = semantic_web_pygments.sw:Notation3Lexer
"""
)
