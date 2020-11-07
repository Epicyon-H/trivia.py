import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="trivia.py",
    version="1.0.6",
    description="A python wrapper for Open Trivia DB",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Epicyon-H/trivia.py",
    author="Epicyon",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=['trivia'],
    include_package_data=True,
    install_requires=["aiohttp", "aiodns"],
)
