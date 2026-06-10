from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, description="The item name")
    description: Optional[str] = Field(None, description="A short item description")
    price: float = Field(..., gt=0, description="The item price")

class Item(ItemBase):
    id: int

items = [
    Item(id=1, name="Sample Item", description="A starter item", price=9.99)
]

@app.get("/items", response_model=List[Item], summary="List all items")
def read_items(q: Optional[str] = Query(None, description="Filter items by name")):
    if q:
        return [item for item in items if q.lower() in item.name.lower()]
    return items

@app.get("/items/{item_id}", response_model=Item, summary="Get a single item")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201, summary="Create a new item")
def create_item(item: ItemBase):
    new_id = max([existing.id for existing in items], default=0) + 1
    new_item = Item(id=new_id, **item.dict())
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item, summary="Update an existing item")
def update_item(item_id: int, item: ItemBase):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            updated_item = Item(id=item_id, **item.dict())
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", summary="Delete an item")
def delete_item(item_id: int):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            items.pop(index)
            return {"detail": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
