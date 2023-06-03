from typing import Any
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from ..services import ListRepresentation


class ToDo(View):
    def __init__(self, **kwargs: Any) -> None:
        self.item_obj: ListRepresentation = ListRepresentation()
        super().__init__(**kwargs)

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if request.method.lower() == "get" and "id" in kwargs:
            return self.get_element_by_id(request, id=int(kwargs["id"]))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest):
        return self.item_obj.get_all_elements()

    def get_element_by_id(self, request: HttpRequest, id: int):
        if not (item := self.item_obj.get_element_by_id(id=int(id))):
            return item

        return item

    def post(self, request: HttpRequest):
        item = request.body
        if not item:
            return HttpResponse(JsonResponse({"Error": "No item"}), status=400)

        return self.item_obj.update_items(item)

    def put(self, request: HttpRequest, id: int):
        new_item = request.body

        if not (item := self.item_obj.update_list_item(new_item, id)):
            return item

        return item

    def delete(self, request: HttpRequest, id: int):
        return self.item_obj.delete_list_item(id)
