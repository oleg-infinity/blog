import os

PATH = os.path.dirname(__file__) + os.sep
PATH_STATIC = PATH + "static" + os.sep

SECRET_KEY = os.urandom(24)