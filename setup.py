from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tst-trn-splt", # the name that you will install via pipenv
    version="1.0",
    author="Jason Robinson",
    author_email="jasonrobinson988@gmail.com",
    description="A brief overview of the steps...",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/techthumb1/lambdata_techthumb1.git",
    #keywords="",
    packages=find_packages() # ["lambdata_techthumb1"]
)