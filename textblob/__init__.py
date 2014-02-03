import os

__version__ = '0.8.4'
__license__  = 'MIT'
__author__ = 'Steven Loria'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

from .blob import TextBlob, Word, Sentence, Blobber, WordList
