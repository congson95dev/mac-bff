import string

from flask import request
from flask_accepts import accepts, responds
from flask_restx import Resource, Namespace

from src.common.response import Responses
from src.schemas.ToDoList.ToDoListSchema import (
    ToDoListCreateRequestSchema,
    ToDoListFilterQuerySchema,
    ToDoListFilterResponseSchema,
    ToDoListGetCreateUpdateResponseSchema,
)
from src.service.ToDoListService import ToDoListService

api = Namespace(
    "To do list",
    description="To do list related operations",
)


@api.route("/")
class ToDoLists(Resource):
    @api.doc("Get To Do List")
    @accepts(query_params_schema=ToDoListFilterQuerySchema, api=api)
    @responds(schema=ToDoListFilterResponseSchema, api=api, status_code=200)
    def get(self):
        params = request.args.to_dict()
        response = ToDoListService.get_list_to_do_list_by_search_params(params)
        return Responses.ok_response(response)

    @api.doc("Create To Do List")
    @accepts(schema=ToDoListCreateRequestSchema, api=api)
    @responds(schema=ToDoListGetCreateUpdateResponseSchema, api=api)
    def post(self):
        data = request.get_json()
        response_data = ToDoListService.create_to_do_list(data)
        return Responses.ok_response(response_data)


@api.route("/<string:id>")
class ToDoListDetail(Resource):
    @api.doc("Get detail To Do List by id")
    @responds(schema=ToDoListGetCreateUpdateResponseSchema, api=api, status_code=200)
    def get(self, id: string):
        response = ToDoListService.get_to_do_list_by_id(id)
        return Responses.ok_response(response)

    @api.doc("Update To Do List by id")
    @accepts(schema=ToDoListCreateRequestSchema, api=api)
    @responds(schema=ToDoListGetCreateUpdateResponseSchema, api=api, status_code=200)
    def put(self, id: string):
        data = request.json
        response_data = ToDoListService.update_to_do_list(data, id)
        return Responses.ok_response(response_data)

    @api.doc("Delete To Do List by id")
    def delete(self, id: string):
        ToDoListService.delete_to_do_list(id)
        return Responses.ok_response_without_data()


@api.route("/<string:id>/mark-done")
class ToDoListMarkDone(Resource):
    @api.doc("Mark done To Do List by id")
    def put(self, id: string):
        ToDoListService.mark_done_to_do_list(id)
        return Responses.ok_response_without_data()
