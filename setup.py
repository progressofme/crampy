from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
import os

setup(name='andrew',
      version='0.01',
      description='Crampy',
      url='https://github.com/progressofme/crampy',
      author='Anonymous',
      author_email='contactcrampy@gmail.com',
      license='MIT',
      install_requires=[],
      setup_requires=[],
      packages=['crampy'],
      zip_safe=False)
