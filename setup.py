import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="curve_method",
    version="v0.2.1",
    description="A quantitative approach to select the optimal number of clusters in a dataset.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/alexjfreund/curve_method",
    download_url="https://github.com/alexjfreund/curve_method/archive/v0.2.1.tar.gz",
    author="Alex Freund",
    author_email="alexjfreund@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    packages=["curve_method"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib", "scikit-learn"]
)
