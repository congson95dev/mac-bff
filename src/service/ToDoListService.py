from src.common.handle_exception import NotFoundException, BadRequestException
from src.service.GrpcService import GrpcService


class ToDoListService:
    @staticmethod
    def get_list_to_do_list_by_search_params(params):  # noqa C901
        search = (
            "%{}%".format(params.get("search").strip())
            if params.get("search")
            else None
        )
        page = params.get("page") or 1
        size = params.get("size") or 20

        to_do_lists = GrpcService.grpc_to_do_list(search, page, size)

        response_data = []
        for to_do_list in to_do_lists:
            to_do_list_dict = {
                "id": to_do_list.get("id"),
                "title": to_do_list.get("title"),
                "description": to_do_list.get("description"),
                "status": to_do_list.get("status"),
            }
            response_data.append(to_do_list_dict)

        total = len(to_do_lists)

        return {
            "items": response_data,
            "page_size": int(size),
            "page": int(page),
            "total": total,
        }

    @staticmethod
    def create_to_do_list(data):
        to_do_list = GrpcService.grpc_to_do_create(data)

        response_data = {
            "id": to_do_list.get("id"),
            "title": to_do_list.get("title"),
            "description": to_do_list.get("description"),
            "status": to_do_list.get("status"),
        }

        return response_data

    @staticmethod
    def get_to_do_list_by_id(id: int):
        to_do_list = GrpcService.grpc_to_do_view_detail(id)
        if to_do_list.get("status_code") == 404:
            raise NotFoundException(message=f"To Do List with id {id} not found")

        return {
            "id": to_do_list.get("id"),
            "title": to_do_list.get("title"),
            "description": to_do_list.get("description"),
            "status": to_do_list.get("status"),
        }

    @staticmethod
    def update_to_do_list(data, id: int):  # noqa: C901
        to_do_list = GrpcService.grpc_to_do_update(data, id)

        # check if to_do_list with given id exists, if not, throw error
        if to_do_list.get("status_code") == 404:
            raise NotFoundException(message=f"To Do List with id {id} not found")

        return {
            "id": to_do_list.get("id"),
            "title": to_do_list.get("title"),
            "description": to_do_list.get("description"),
            "status": to_do_list.get("status"),
        }

    @staticmethod
    def delete_to_do_list(id: int):
        GrpcService.grpc_to_do_delete(id)

    @staticmethod
    def mark_done_to_do_list(id: int):
        GrpcService.grpc_to_do_mark_done(id)
