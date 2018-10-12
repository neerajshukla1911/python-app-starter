from celery import Celery
from config_reader import get_config

config = get_config('celery_app')

celery_app = Celery(config['env'])

celery_app.conf.update(config)

from .tasks import *

