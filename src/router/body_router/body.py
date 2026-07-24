from typing import Annotated, Any

from fastapi import APIRouter, Path, Query, Body
from fastapi.openapi.models import Example

from vm.item_vm import Item, User, Offer

BODY_ROUTER = APIRouter(prefix="/body", tags=["查詢參數模型"])


# 混用 Path、Query 與 Body 參數，沒指定參數來源的話，FastAPI 預設把簡單型別視為 Query
@BODY_ROUTER.put("/update_item")
def update_item(
        item_id: Annotated[int, Path(title="這是id", ge=0, le=100)],
        item: Annotated[Item | None, Body(openapi_examples={
            "a": Example(  # 使用 Example 物件包起來
                summary="一般範例",
                value={
                    "name": "Test_1",
                    "description": "描述1",
                    "price": 35.2,
                    "tax": 5.7,
                    "tags": ["aaa", "bbb"],
                    "image": [
                        {"url": "https://example1.com/baz.jpg", "name": "The Baz"}
                    ],
                },
            ),
            "b": Example(
                summary="警告範例",
                value={
                    "name": "Test_2",
                    "description": "描述2",
                    "price": 15.2,
                    "tax": 1.0,
                    "tags": ["ccc", "sss"],
                    "image": [
                        {"url": "https://example2.com/baz.jpg", "name": "The Cat"},
                        {"url": "https://example3.com/baz.jpg", "name": "The Dog"}
                    ],
                },
            )
        }
        )] = None,
        q: Annotated[str | None, Query(examples=["參數1", "參數2"])] = None,
):
    """

    :param item_id: 型別為整數的 item_id
    :param q: 型別為字串的 q
    :param item: 請看 vm 中的 item_vm 檔案
    :return: 回傳字典
    """
    results: dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# 套用多個 Body 來源
@BODY_ROUTER.put("/multi_update_item")
def multi_update_item(
        item_id: Annotated[int, Query(title="這是id", ge=0, le=100)],
        item: Item,
        user: User
):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user
    }

    print(results)

    return results


@BODY_ROUTER.post("/offers")
def create_offers(offers: Offer):
    print(offers)
    return offers
