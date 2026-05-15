from flask import Flask

app = Flask(__name__)

items = {
    '1': {"name": "Item 1"},
}

@app.post("/items/")
def create_item(item: dict):
    items[len(items)] = item
    return {"item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"item_id": item_id, "status": "deleted"}
    return {"error": "Item not found"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if item_id in items:
        items[item_id] = item
        return {"item_id": item_id, "item": item, "status": "updated"}
    return {"error": "Item not found"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in items:
        return {"item_id": item_id, "name": f"Item {item_id}"}
    return {"error": "Item not found"}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</>"
