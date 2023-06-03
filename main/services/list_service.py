from django.http import HttpResponse, JsonResponse
from jsonschema import validate, ValidationError
import json


class ListRepresentation:
    id: int = 1

    items = []

    def __init__(self):
        self._item_schema: map = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "body": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "activity": {"type": "string"},
                        "done": {"type": "boolean"},
                    },
                    "required": ["title", "activity", "done"],
                },
            },
        }

        self._updated_item_schema: map = {
            "type": "object",
            "properties": {
                "body": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "activity": {"type": "string"},
                        "done": {"type": "boolean"},
                    },
                },
            },
            "required": ["body"],
        }

    def get_all_elements(self) -> HttpResponse:
        if not self.items:
            return HttpResponse(JsonResponse({"Error": "No items"}), status=404)

        return HttpResponse(json.dumps(self.items), status=200)

    def get_element_by_id(self, id: int) -> HttpResponse:
        item = [item for item in self.items if item["id"] == id]
        if item:
            return HttpResponse(json.dumps(item), status=200)
        return HttpResponse(JsonResponse({"Message": "Element not found"}), status=404)

    def _item_validation(self, item: str) -> bool:
        try:
            validate(instance=json.loads(item), schema=self._item_schema)
            return True
        except ValidationError:
            return False

    def update_items(self, item) -> HttpResponse:
        self.schema = {"id": self.id}
        self.schema.update(json.loads(item))
        ListRepresentation.id += 1
        self.id = ListRepresentation.id

        if not self._item_validation(item):
            return HttpResponse(JsonResponse({"Error": "Item out pattern"}), status=400)

        self.items.append(self.schema)

        return HttpResponse(json.dumps(self.schema), status=200)

    def _item_update_validation(self, updated_item) -> bool:
        try:
            validate(
                instance=json.loads(updated_item), schema=self._updated_item_schema
            )
            return True
        except ValidationError:
            return False

    def update_list_item(self, updated_item, id) -> HttpResponse:
        if not self._item_update_validation(updated_item):
            return HttpResponse(
                JsonResponse({"Message": "Element out of pattern"}), status=400
            )

        updated_item: dict = json.loads(updated_item)
        for item in self.items:
            if item["id"] == id:
                if "title" in updated_item["body"]:
                    item["body"]["title"] = updated_item["body"]["title"]
                if "activity" in updated_item["body"]:
                    item["body"]["activity"] = updated_item["body"]["activity"]
                if "done" in updated_item["body"]:
                    item["body"]["done"] = updated_item["body"]["done"]
                return HttpResponse(json.dumps(item), status=200)
        return HttpResponse(JsonResponse({"Message": "Element not found"}), status=404)

    def delete_list_item(self, id: int) -> HttpResponse:
        for item in self.items:
            if item["id"] == id:
                self.items.remove(item)
                return HttpResponse(JsonResponse({"Element deleted": item}), status=200)

        return HttpResponse(JsonResponse({"Message": "Element not found"}), status=404)
