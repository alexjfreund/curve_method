import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="curve_method",
    version="0.1.0",
    description="A quantitative approach to select the optimal number of clusters",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/alexjfreund/curve-method",
    author="Alex Freund",
    author_email="alexjfreund@gmail.com",
    licence="MIT",
    classifiers=[
        "Licence :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages=["curve_method"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib", "scikit-learn"]
)