import os
import json
import logging
from flask_restful import Resource


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")


class CheckController(Resource):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def get(self):
        with open(os.path.join(RESOURCES_DIR, "response.json"), encoding="utf-8") as f:
            response_template = json.loads(f.read())
            return response_template.get("data")
