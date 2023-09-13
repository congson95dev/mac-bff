from marshmallow import Schema, fields
from marshmallow.fields import DateTime

from src.common.common import DATE_TIME_FORMAT
from src.common.response import BaseResponseSchema


# request for get all api
class ToDoListFilterQuerySchema(Schema):
    search = fields.String()
    page = fields.Integer()
    size = fields.Integer()


# response for get all api
class ToDoListFilterInSchema(Schema):
    id = fields.String(required=True)
    title = fields.String(required=True)
    description = fields.String(required=False)
    status = fields.String(required=True)


# response for get all api
class ToDoListFilterDataSchema(Schema):
    items = fields.List(fields.Nested(ToDoListFilterInSchema))
    total = fields.Integer(required=True)
    page_size = fields.Integer(required=True)
    page = fields.Integer(required=True)
    last_update = DateTime(required=True, format=DATE_TIME_FORMAT)


# response for get all api
class ToDoListFilterResponseSchema(BaseResponseSchema):
    data = fields.Nested(ToDoListFilterDataSchema)


# request for create api and update by id api
class ToDoListCreateRequestSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=False)


# response for get by id api, create api, update api
class ToDoListGetCreateUpdateResponseSchema(BaseResponseSchema):
    data = fields.Nested(ToDoListFilterInSchema)
