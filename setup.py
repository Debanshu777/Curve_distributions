from pathlib import Path

from setuptools import setup

# The directory containing this file

HERE :Path = Path(__file__).parent

# The text of the README file
# The text of the README file is used as the long_description for the package

README :str = (HERE /"curve_distributions/README.md").read_text()

# This call to setup() does all the work

setup(

    name="curve_distributions",

    version="0.3",

    description="Various functions on Gaussian and Binomial distributions",

    long_description=README,

    long_description_content_type="text/markdown",

    url="https://github.com/Debanshu777/Curve_distributions",

    author="Debanshu777",

    author_email="debanshudatta123@gmil.com",

    license="MIT",

    classifiers=[
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",

        "Programming Language :: Python :: 3.7",
    ],

    packages=["curve_distributions"],

    zip_safe=False
)