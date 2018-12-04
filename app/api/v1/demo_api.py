from sanic.response import json
import logging
from app import config

logger = logging.getLogger(__name__)


async def demo_api(request):

    logger.debug("**************{}".format(config['DEFAULT']['env']))
    return json({"hello": "world"})
