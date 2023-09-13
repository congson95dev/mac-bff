from flask import Flask
from flask_restx import Api
from src.common.handle_exception import handle_exception


app = Flask(__name__)

# set this so when we return jsonify in api, it will not sort the result by alphabelt
app.config["JSON_SORT_KEYS"] = False

# add handle exception
handle_exception(app)

# init api from flask_restx
api = Api(app)

# we import this files at the end of the file because in those file,
# we call some variable of this __init__.py file inside it
# such as variable "api"
import src.apis.base
