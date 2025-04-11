# setup.py
import os
import sys
from setuptools import setup, find_packages

# SDK metadata
pkg_name = 'xpens'
directory = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(directory, pkg_name))

# Read the long description from README.md
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xpens-sdk',
    version='0.1.0',
    description='Python SDK for interacting with XPENS.AI APIs',
    author='XPENS.AI',
    url='https://github.com/xpensai/xpens-sdk',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic",
        'python-dotenv'
    ],
    python_requires='>=3.8',
)
