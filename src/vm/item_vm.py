from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str = Field(examples=["photo", "image"])

    model_config = {
        "frozen": True,
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://www.google.com/",
                    "name": "example_name"
                }
            ]
        }
    }


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float= Field(examples=[35.4])
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
