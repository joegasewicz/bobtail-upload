from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="bobtail-upload",
    version="0.0.1",
    description="File Uploads for Bobtail",
    packages=["bobtail_upload"],
    py_modules=["bobtail_upload"],
    install_requires=[
        "bobtail"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/bobtail-upload",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com"
)