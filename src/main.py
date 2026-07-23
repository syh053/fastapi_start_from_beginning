from fastapi import FastAPI

from router.center import CENTER_ROUTER

WEB_SERVER_SETTING = {
    "app": "main:app",
    "host": "127.0.0.1",
    "port": 8888,
    "reload": True,
    "reload_excludes": [".venv"],
}

app = FastAPI()

app.include_router(CENTER_ROUTER)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(**WEB_SERVER_SETTING)
