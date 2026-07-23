from fastapi import UploadFile


class ImgService:
    async def create_img(self, file: UploadFile):
        """
        接收來自前端上傳的圖片檔案，並回傳儲存後的檔案名稱

        :param file: 傳信來的檔案
        :return: 檔案名稱
        """
        return f"{file.filename}"
