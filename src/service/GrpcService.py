from src.common.common import Common


class GrpcService:
    @staticmethod
    def grpc_to_do_list(search, page, size):
        # logic to call grpc

        # logic to convert from grpc to rest
        response = {
            "todos": [
                {
                    "id": "01HA4EQVW6WM0P15BB7KAYND2B",
                    "title": "to do list 1",
                    "description": "description 1",
                    "status": "created",
                },
                {
                    "id": "01HA4EQV5VE7J0R2JYTZ0ZR169",
                    "title": "to do list 2",
                    "description": "description 2",
                    "status": "created",
                },
                {
                    "id": "01HA4EQT6C10V9BWT2FK1HM41S",
                    "title": "to do list 3",
                    "description": "description 3",
                    "status": "created",
                },
                {
                    "id": "01HA4BK8R745YPFD4Z81FTBNTC",
                    "title": "to do list 4",
                    "description": "description 4",
                    "status": "created",
                },
                {
                    "id": "01HA49P9CW22BK47MQDJWCMNJZ",
                    "title": "to do list 5",
                    "description": "description 5",
                    "status": "done",
                },
            ]
        }

        return response["todos"]

    @staticmethod
    def grpc_to_do_create(data):
        # logic to call grpc

        # logic to convert from grpc to rest
        response = {
            "id": "01HA63SSTEWGZK1EQXAJXS5SX1",
            "title": "to do list 6",
            "description": "description 6",
            "status": "created",
        }

        return response

    @staticmethod
    def grpc_to_do_update(data, id):
        # logic to call grpc

        # logic to convert from grpc to rest
        response = {
            "id": "01HA4EQT6C10V9BWT2FK1HM41S",
            "title": "to do list 7",
            "description": "description 7",
            "status": "done",
        }

        # get status_code from response
        response["status_code"] = 0

        # convert grpc status code to rest status code
        response["status_code"] = Common.change_status_code(response.get("status_code"))

        return response

    @staticmethod
    def grpc_to_do_view_detail(id):
        # logic to call grpc

        # logic to convert from grpc to rest
        response = {
            "id": "01HA4EQT6C10V9BWT2FK1HM41S",
            "title": "to do list 7",
            "description": "description 7",
            "status": "done",
        }

        # get status_code from response
        response["status_code"] = 0

        # convert grpc status code to rest status code
        response["status_code"] = Common.change_status_code(response.get("status_code"))

        return response

    @staticmethod
    def grpc_to_do_delete(id):
        # logic to call grpc

        # logic to convert from grpc to rest
        response = {}

        return response

    @staticmethod
    def grpc_to_do_mark_done(id):
        # logic to call grpc

        # logic to convert from grpc to rest
        response = {}

        return response
