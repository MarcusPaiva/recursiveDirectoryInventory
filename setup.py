import setuptools
from datetime import date

with open("README.md", "r") as f:
    long_description = f.read()

NAME = "directoryInventory"
URL = "https://github.com/MarcusPaiva/recursiveDirectoryInventory"
VERSION = date.today().strftime("%Y.%#m.%#d")

AUTHOR = "Marcus Paiva"
AUTHOR_EMAIL = "marcus.paiva.ti@gmail.com"

DESCRIPTION = "This repository contains a reader contents of directory, but read contants directory inside directory " \
              "and show all data, directory size and other things"

setuptools.setup(
    name=NAME,
    url=URL,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[],
)
