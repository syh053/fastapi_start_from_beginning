from fastapi import APIRouter

from router.img_router.img import FILE_ROUTER

CENTER_ROUTER = APIRouter()
CENTER_ROUTER.include_router(FILE_ROUTER)


@CENTER_ROUTER.get("/hello")
def say_hello(name: str):
    return f"Hello {name}."
