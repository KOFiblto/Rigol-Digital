import setuptools
from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Rigol1000z',
    version='0.2.2',
    author="Jean Yves Beaucamp (@jeanyvesb9), @jtambasco",
    author_email="jeanyvesb9@me.com",
    description="Python VISA (USB and Ethernet) library to control Rigol DS1000z series oscilloscopes.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jeanyvesb9/Rigol1000z",
    packages=['rigol1000z'],
)
