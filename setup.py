import sys
import platform
from distutils.core import setup

if sys.version_info < (3,7):
    print('This build is for Python3.7. Aborting.')
    exit()

if platform.architecture() != ('64bit', 'WindowsPE'):
    print('This installer is only for 64bit Windows. Aborting')
    exit()

setup(
    name = "yara",
    author = "Kiran Bandla",
    author_email = "kbandla@in2void.com",
    version = "3.8.1",
    description = "Python bindings for yara as a DLL",
    long_description = "Python/C Wrapper for the yara library",
    url = "http://www.github.com/kbandla/yara-python37",
    packages = ['libyara'],
    package_data={'libyara': ['*.dll', 'yara.pyd']},
)