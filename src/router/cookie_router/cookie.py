from typing import Annotated

from fastapi import APIRouter, Cookie

from vm.cookie_vm import Cookies

COOKIE_ROUTER = APIRouter(prefix="/cookie", tags=["餅乾"])


@COOKIE_ROUTER.get("")
def read_cookie(cookies: Annotated[Cookies, Cookie]):
    print(cookies)
    return cookies