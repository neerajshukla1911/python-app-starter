import configparser
import os


def get_config():
    CONFIG_FILE = os.environ.get("CONFIG_FILE", 'config_files/config.dev.ini')
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config.read(CONFIG_FILE)
    return config