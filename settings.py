# settings.py
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    """ Base configurations """
    BASE_URL = os.environ.get('BASE_URL') or 'a'
    USERNAME = os.environ.get('USERNAME') or 'b'
    PASSWORD = os.environ.get('PASSWORD') or 'c'