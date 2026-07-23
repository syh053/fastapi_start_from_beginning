from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile

from service.img_service.post_img import ImgService
from tools.service_provider import service_provide

FILE_ROUTER = APIRouter(prefix="/photo", tags=["照片處理路由"])

IMG_SERVICE = Annotated[ImgService, Depends(service_provide(ImgService))]


@FILE_ROUTER.post("")
async def create_img(
        service: IMG_SERVICE,
        file: UploadFile
):
    return await service.create_img(file=file)
