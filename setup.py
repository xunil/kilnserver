import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "kilnserver",
    version = "0.0.1",
    author = "Robert Liesenfeld",
    author_email = "xunil@xunil.net",
    description = ("Daemon and web interface for controlling heat-treating and ceramics kilns."),
    license = "Proprietary",
    keywords = "thermocouple fuzzy-logic heat-treat kiln",
    url = "http://xunil.net/",
    packages=['kilnserver'],
    install_requires=[
      'Flask >= 0.10.1',
      'Flask-SQLAlchemy >= 1.0'
    ],
    entry_points={
        'console_scripts': [
            'web = kilnserver:main',
            'kiln = kilnserver.kiln_controller:main',
        ],
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: Other/Proprietary License",
    ],
)