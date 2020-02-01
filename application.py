import os
import logging
from flask import Flask, request, abort, redirect, make_response
from flask_restful import Api
from api_resources.resources import resources

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resources")

logging.basicConfig(
    format=u'%(filename)s\t[LINE:%(lineno)d]# %(levelname)-8s\t [%(asctime)s]  %(message)s',
    level=logging.DEBUG)

app = Flask(__name__)
api = Api(app=app, prefix="/api/v1/")

# add api_resources
for resource in resources:
    api.add_resource(resource.get_cls(), resource.get_url())


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=8080)
