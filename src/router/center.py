from typing import Annotated, Any

from fastapi import APIRouter, Query, Path

from router.body_router.body import BODY_ROUTER
from router.img_router.img import FILE_ROUTER
from vm.item_vm import Item

CENTER_ROUTER = APIRouter()
CENTER_ROUTER.include_router(FILE_ROUTER)
CENTER_ROUTER.include_router(BODY_ROUTER)


@CENTER_ROUTER.get("/hello")
def say_hello(name: str):
    return f"Hello {name}."


@CENTER_ROUTER.get("/items/{item_id}")
def read_item(item_id: int):
    """
    收到 query 並回傳整數

    :param item_id: 傳入 item (整數)
    :return:
    """
    return f"item_id :{item_id}"


@CENTER_ROUTER.get("/info")
def get_item(name: str, age: int, sex: bool, description: str | None = None):
    """
    取得請求 ? 後面的 name 及 age，

    :param name: 使用者名稱
    :param age: 使用者年齡
    :param sex: 使用者性別
    :param description: 描述
    :return: 回傳使用者字典格式的資料
    """
    return {
        "name": name,
        "age": age,
        "sex": sex,
        "description": description
    }


@CENTER_ROUTER.post("/item")
def create_item(item: Item):
    """
    建立 item

    :param item: 傳入 item，型別可以參照 vm 資料夾中的 item_vm 檔案中察看
    :return: 回傳建立的 item 字典
    """
    dict_item = item.model_dump(exclude={"description"})
    return dict_item


@CENTER_ROUTER.get("/item_with_query")
def item_with_query(q: Annotated[int | None, Query(lt=50)] = 10):
    """
    將傳入的請求 q 用字典的方式回傳

    :param q: 請求傳入的數值，預設值是 10
    :return: 回傳 q
    """
    return {"q": q}


@CENTER_ROUTER.get("/list_item_query")
def item_with_query(
        word: Annotated[
            list[str] | None, Query(title="這是變數", description="變數描述", alias="item-query", max_length=50)] = [
            "foo", "bar"
        ]
):  # type: ignore
    """
    將傳入的請求 word 用字典的方式回傳

    :param word: 請求傳入的字串，預設值是 None
    :return: 回傳 word
    """
    print(word)
    return {"word": word}


@CENTER_ROUTER.get("/item_with_path/{item_id}")
def read_item_with_path(
        item_id: Annotated[int, Path(title="這是 ID")],
        q: Annotated[str | None, Query(alias="item-query")] = None
):
    results: dict[str, Any] = {"item_id": item_id}

    if q:
        results.update({"q": q})
    return results


@BODY_ROUTER.get("/filter")
def body_filter(filter_query: Annotated[Filter, Query()]):
    print(filter_query)
    return {**filter_query.model_dump()}
