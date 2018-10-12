import configparser
import os


def get_config(config_type):
    CONFIG_FILE = os.environ.get("CONFIG_FILE", 'config/config.dev.ini')
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config.read(CONFIG_FILE)
    return config[config_type]