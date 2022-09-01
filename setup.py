"""
setup.py -  setuptools configuration for esc
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tiw",
    version="0.0.3",
    author="ibby",
    author_email="theibbster@proton.me",
    description="Tooling for my TiddlyWiki, forked from sobjornstad/tzk ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PARC6502/tiw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "tiw = tzk.__main__:launch"
        ],
    },
    python_requires='>=3.6',
    include_package_data=True,
)
