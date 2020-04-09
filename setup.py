#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r", encoding='utf8') as file:
      long_description = file.read()

setup(name='dev_aberto_martimfj',
      version='0.2',
      author='Martim Jose',
      author_email="martimfj@al.insper.edu.br",
      description="Pacote de exemplo Dev-Aberto",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/martimfj/dev_aberto_package",
      packages=['dev_aberto'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      install_requires=[
            'requests'
      ],
      scripts=['scripts/hello.py'],
      )
