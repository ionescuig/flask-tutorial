'''Configuration File'''
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    '''Main Class'''
    #SECRET KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # EMAIL
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['gabriel.ionescu@landregistry.gov.uk']

    # POSTS PER PAGE
    POSTS_PER_PAGE = 10

    # LANGUAGES
    LANGUAGES = ['en', 'es', 'ro']

    # TRANSLATION
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    # ELASTICSEARCH
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    # LOG TO STDOUT
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    print('>>> [config] >>> LOG_TO_STDOUT:', LOG_TO_STDOUT)
    