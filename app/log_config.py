from config_reader import get_config

config = get_config()


def get_log_config():
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': config['logging']['log_file_name'],
                'maxBytes': 1024 * 1024 * 50,
                'backupCount': 10,
                'formatter': 'file'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
        },
        'formatters': {
            'file': {
                'format': '[%(asctime)s][%(levelname)s] %(name)s '
                          '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
                'datefmt': '%H:%M:%S',
            },
            'console': {
                'format': '[%(asctime)s][%(levelname)s] %(name)s '
                          '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
                'datefmt': '%H:%M:%S',
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['file', 'console'],
                'propagate': True
            },
        }
    }
    return log_config
