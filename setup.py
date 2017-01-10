from setuptools import setup

setup(
    name='Filter',
    version='0.1',
    author='Valentin Jacquemin',
    author_email='jacqueminv@gmail.com',
    packages=['filter', 'filter.model', 'filter.pyExcelerator'],
    app=['run.py'],
    data_files=[],
    setup_requires=['py2app']
)
