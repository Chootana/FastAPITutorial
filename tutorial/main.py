from typing import Optional
from typing import List

from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

app = FastAPI()


@app.get("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

@app.get("/items/")
async def read_items(q: Optional[str] = Query(..., min_length=3)):
    results = {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ]
    }

    if q:
        results.update({"q": q})
    
    return results

@app.get("/items2/")
async def read_items2(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

@app.get("/items3/{item_id}")
async def read_items3(
    *,
    item_id: int = Path(..., title="The ID of the item to get"),
    q: str
):
    results = {"item_id": item_id}

    if q:
        results.update({"q": q})
    
    return results

@app.get("/items4/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body(...)):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
