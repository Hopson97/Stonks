from setuptools import setup

setup(
    name='pystonks',
    version='1.0',
    description='stonks',
    author='Hopson97',
    url='https://github.com/Hopson97/Stonks/',
    packages=['stonks'],
    entry_points={
        "console_scripts": [
            "stonks = stonks:main"
        ]
    }
)
