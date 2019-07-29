import setuptools
import io
import os
import sys

required = ['redis']

here = os.path.abspath(os.path.dirname(__file__))

with open("read-config/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="read_config",
    version="0.0.5",
    author="Jason Duncan",
    author_email="jason.matthew.duncan@gmail.com",
    description="Read redis DB config for other modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jduncan8142/read_config",
    install_requires=required,
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_data={'read-config': ['requirements.txt', 'README.md', 'LICENSE']},
    py_modules=[
        'read-config.py'
    ],
)
