# 64bit yara-python for Windows 

In migrating to Python3.7 x64, I discovered that yara-python does not have 
a build for it. So I built one for myself. 

This is a build of yara-python for Windows x64, and Python 3.7 x64:

* uses stock yara-python, but built for Python 3.7
* it uses libyara64 - yara as a 64bit DLL
  * uses 64bit OpenSSL for the Hash Module

## Requirements

* 64-bit Windows 
* 64-bit Python 3.7

## Installation

> python setup.py install


## Usage

Everything is the same as `yara-python`, except the initial import:

> from libyara import yara

