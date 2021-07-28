# coding=utf-8

from setuptools import setup, find_packages
import os

import tools

for big_file in tools.BIG_FILES:
    tools.join(big_file)

appname = "text_recognition_system"
version = "1.0.0"

try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
except:
    readme = ""

packages = ["text_recognition_system", "libtorch"]

setup(
    name=appname,
    version=version,
    description=(
        '''%s''' % appname
    ),

    author='Shantilata Dey',
    author_email='shantilatadey143@gmail.com',
    maintainer='Shantilata Dey',
    maintainer_email='shantilatadey143@gmail.com',
    packages=packages,
    platforms=["linux"],
    url='https://pypi.org/project/%s/' % appname,
    classifiers=[],
    install_requires=[],
    include_package_data=True,

    long_description=readme,
    long_description_content_type='text/markdown'
)
