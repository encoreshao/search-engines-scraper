from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    # Application name:
    name='search_engines',

    # Version number (initial):
    version='0.0.1',

    # license="LICENSE.txt",
    description='Search Engines Scraper',
    # long_description=open("README.txt").read(),

    # Application author details:
    author='Encore. S',
    license='MIT',

    # Include additional files into the package
    include_package_data=True,

    packages=find_packages(),
    install_requires=requirements
)
