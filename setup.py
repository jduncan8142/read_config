import setuptools

install_requires = ['redis']

packages = ["read_config"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="read_config",
    version="0.0.3",
    author="Jason Duncan",
    author_email="jason.matthew.duncan@gmail.com",
    description="Read redis config DB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jduncan8142/read_config",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English"
    ],
    install_requires=install_requires,
)
