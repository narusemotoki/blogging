__author__ = 'Motoki Naruse'
__version__ = '0.0.2'
__license__ = 'MIT'

import logging.handlers
import types
from logging import *  # noqa


log_levels = {
    'critical': CRITICAL,
    'error': ERROR,
    'warning': WARNING,
    'info': INFO,
    'debug': DEBUG,
    'notset': NOTSET,
}
default_log_format = Formatter(
    '%(levelname)s %(name)s - %(asctime)s - File: %(pathname)s - Line: %(lineno)d'
    '- Func: %(funcName)s Message: %(message)s'
)


def init(config: dict, name: str=None) -> Logger:
    def create_handler(function: types.FunctionType, config: dict) -> Handler:
        if config is None:
            return None

        handler = function(config)
        handler.setLevel(log_levels[config['level']])
        handler.setFormatter(config.get('log_format', default_log_format))
        return handler

    def create_file_hander() -> Handler:
        return create_handler(
            lambda config: FileHandler(filename=config['filepath'], encoding='UTF-8'),
            config.get('file')
        )

    def create_email_handler() -> Handler:
        return create_handler(lambda config: logging.handlers.SMTPHandler(
            mailhost=(config['smtp_host'], config['smtp_port']),
            fromaddr=config['email_from'],
            toaddrs=(config['email_to'], ),
            subject=config['email_subject'],
            credentials=(config['smtp_username'], config['smtp_password']),
            secure=()
        ), config.get('email'))

    logger = getLogger(name)
    logger.setLevel(NOTSET)

    for function in [create_file_hander, create_email_handler]:
        hundler = function()
        if hundler is not None:
            logger.addHandler(hundler)

    return logger
