from setuptools import setup
from os import path
import codecs

this_directory = path.abspath(path.dirname(__file__))

def read(rel_path):
    this_directory = path.abspath(path.dirname(__file__))
    with codecs.open(path.join(this_directory, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version")

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='stockSim',
      url='https://github.com/killkelleyr/stock_sim',
      version=get_version("stock_sim/__init__.py"),
      python_requires=">=3",
      entry_points = {'console_scripts': [
          'stockSim = stock_sim.cli.stockSim:main']},
      packages=['stock_sim/modules'],
      description='',
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False,
      install_requires=[
          'numpy',
          'mysql-connector-python',
          'yfinance',
          'pandas'])
