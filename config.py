import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'b65de5f006a1d744f90e6d67c8727e532afb12c5'