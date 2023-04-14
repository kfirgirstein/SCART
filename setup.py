from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='scart',
    version='1.0.0',
    description='SCART: Simulation of Cyber Attacks for Real-Time systems',
    author='Kfir Girstein',
    author_email='kfirgirstein@campues.technion.ac.il',
    url='https://github.com/kfirgirstein/scart',
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    keywords=['simulation', 'real-time', 'cybersecurity', 'MITM', 'network', 'attacks'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'scart = scart.__main__:main',
        ],
    },
)

