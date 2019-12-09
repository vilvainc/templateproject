
from setuptools import setup, find_packages
from os import path


path_to_here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(path_to_here, 'README.md'), 'r') as f:
    long_description = f.read()

# Project will not be uploaded to PyPI.

setup(
    name="templateproject",  # Replace with your own username
    version="0.0.1",
    author="Data Platform",
    author_email="author@example.com",
    description="Python project template for packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dataplatform/templateproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
