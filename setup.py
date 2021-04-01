from setuptools import setup, find_packages
from pathlib import Path

requirements = []

__version__ = "0.2.0"


# Add README to PyPI
this_dir = Path(__file__).parent
with open(Path.joinpath(this_dir, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="ele",
    version=__version__,
    packages=find_packages(),
    license="MIT",
    author="Ryan S. DeFever",
    author_email="rdefever@nd.edu",
    url="https://github.com/rsdefever/ele",
    install_requires=requirements,
    python_requires=">=3.6, <4",
    include_package_data=True,
    description="A lightweight package with the periodic table of the elements",
    long_description=long_description,
    long_description_content_type="text/x-rst",
)
