from setuptools import setup

setup(
    name="no_set_literals",
    version="0.0.1",
    packages=["no_set_literals"],
    entry_points={
        "console_scripts": ["no-set-literals=no_set_literals.no_set_literals_hook:main"]
    },
)
