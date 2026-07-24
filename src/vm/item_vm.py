from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str

    model_config = {"frozen": True}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: set[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None
    price: float
    items: list[Item]


class User(BaseModel):
    username: str
    full_name: str | None = None


class Filter(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []
