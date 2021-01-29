from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="salnama",
    version="1.0.0",
    author="AbduEbrahimi",
    author_email="a.sanmarin@yahoo.com",
    description="taghvim is a Python(v3.x) library for Calendar and Date Convertor For Persian Date",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbduEbrahimi/salnama",
    packages=find_packages(include=['salnama', 'salnama.*']),
    package_data={'salnama': ['data/taghvim_db.csv']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    			],
     )
