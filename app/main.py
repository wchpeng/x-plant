from fastapi import FastAPI
from app.config.settings import setting
from app.routers import register_router
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from fastapi.staticfiles import StaticFiles


class Router:
    def db_for_read(self, model):
        return "slave"

    def db_for_write(self, model):
        return "master"


def create_app():
    app = FastAPI()

    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

    # 静态文件
    app.mount("/static", StaticFiles(directory="data/static"), name="static")
    register_tortoise(
        app=app,
        config={
            "connections": {
                'master': setting.db_url_master,
                'slave': setting.db_url_slave,
            },
            "apps": {
                "models": {
                    "models": [
                        "app.models.account",
                        "app.models.rhizome",
                    ],
                    "default_connection": "slave",
                }
            },
            "routers": [Router],
            "use_tz": False,
            "timezone": "Asia/Shanghai"
        },
        generate_schemas=True
    )

    register_router(app)

    return app


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', port=8080, reload=True)
