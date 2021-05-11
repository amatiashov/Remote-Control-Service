import os
import json
import logging
from flask_restful import Resource


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")


class CheckController(Resource):
    _logger = None
    _default_response = None

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._default_response = 0

    def get(self):
        try:
            with open(os.path.join(RESOURCES_DIR, "response.json"), encoding="utf-8") as f:
                response_template = json.loads(f.read())
                if not response_template.get("data"):
                    raise RuntimeError("Response template does not contain the 'data' field!")
                return response_template.get("data")
        except Exception as e:
            self._logger.critical("Cannot send data from file: %s" % str(e))
            return self._default_response
