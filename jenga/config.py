import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    PROJECT = 'jenga'
    DEBUG = True

    ADMINS = ['bmwasaru@gmail.com']

    SECRET_KEY = os.environ.get("SECRET_KEY", "u9y32ibckeriy983HH%!^Ii280929juhjbse2")
    CSRF_SESSION_KEY = "878iuibdi228%^JF1ju%^i18991Jhy3iui\Rty"
    WTF_CSRF_SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY", "8jbsdkjjt287yijdskk27^^@uh21")


class DefaultConfig(BaseConfig):
    DEBUG = True
    CSRF_ENABLED = True

    SQLALCHEMY_ECHO = False
    if 'DATABASE_URL' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://jenga:7Ini2yu4H12@localhost'

    MAIL_DEBUG = DEBUG
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USSERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    DEFAULT_SENDER = '%s@gmail.com' % MAIL_USERNAME
