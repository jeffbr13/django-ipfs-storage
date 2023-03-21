import os

from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.abspath(__file__))
README = open(os.path.join(HERE, "README.md")).read()

__version__ = "0.1.0"

setup(
    name="django-ipfs-storage",
    description="IPFS storage backend for Django.",
    long_description=README,
    keywords="django ipfs storage",
    version=__version__,
    license="MPL 2.0",
    author="Ben Jeffrey",
    author_email="mail@benjeffrey.net",
    url="https://github.com/skatepedia/django-ipfs-storage",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Framework :: Django",
    ),
    packages=find_packages(),
    install_requires=(
        "Django",
        "IPFS-Toolkit",
    ),
    test_requires=("pytest"),
)
