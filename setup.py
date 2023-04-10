from setuptools import setup, find_packages

setup(
    name='scart',
    version='0.2',
    description='scart is a tool to generate MITM scripts for network attacks',
    author='Juan Pablo Carrera',
    url='https://github.com/kfirgirstein/scart',
    instal_requires=[],
    packages=find_packages(exclude=['tests']),
)

