from fastapi import FastAPI
from app.config.settings import setting
from app.routers import register_router
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


class Router:
    def db_for_read(self, model):
        if hasattr(model.Meta, 'app'):
            _app = getattr(model.Meta, 'app')
            if _app == 'qiyewx_app':
                return 'qiyewx_slave'
            elif _app == 'mini_admin':
                return 'mini_admin_slave'
        return "slave"

    def db_for_write(self, model):
        if hasattr(model.Meta, 'app'):
            _app = getattr(model.Meta, 'app')
            if _app == 'qiyewx_app':
                return 'qiyewx_master'
            elif _app == 'mini_admin':
                return 'mini_admin_master'
        return "master"


def create_app():
    app = FastAPI()

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

    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

    return app


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', reload=True)
