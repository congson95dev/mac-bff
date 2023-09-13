from src import api
from src.apis.to_do_list.routes import api as book

# create prefix for API
api.add_namespace(book, path="/to-do-list")
