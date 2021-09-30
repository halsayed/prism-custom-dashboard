import os
from decouple import config
from urllib.parse import urljoin


class Config(object):

    API_BASE = 'api/nutanix/v3/'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_123')
    PRISM_HOST = config('PRISM_HOST', default='127.0.0.1')
    PRISM_PORT = config('PRISM_PORT', default=9440, cast=int)
    SSL_VERIFY = config('SSL_VERIFY', default=False, cast=bool)
    HTML_TITLE = config('HTML_TITLE', default='Prism Login')
    LOGIN_HEADER = config('LOGIN_HEADER', default='Custom Prism Login')
    REDIRECT_DEST = config('REDIRECT_DEST', default='console/')
    ATTACH_DOMAIN = config('ATTACH_DOMAIN', default=None)

    BASE_URL = f'https://{PRISM_HOST}:{PRISM_PORT}'
    API_URL = urljoin(BASE_URL, API_BASE)


class ProductionConfig(Config):
    DEBUG = False


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}