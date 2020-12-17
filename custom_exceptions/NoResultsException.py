"""
Name of Program: NoResultsException.py
Author: Ian Tibe
Date of last modification: 12/16/2020

Class definition for NoResultsException
"""


class NoResultsException(BaseException):

    def __init__(self, message=""):
        super().__init__(message)
