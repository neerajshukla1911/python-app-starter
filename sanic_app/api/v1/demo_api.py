from sanic.response import json
import logging

from sanic_app import sanic_app

logger = logging.getLogger(__name__)


async def demo_api(request):

    logger.debug("**************{}".format(sanic_app.config['env']))
    return json({"hello": "world"})
