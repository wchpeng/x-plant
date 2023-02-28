from app.config.settings import setting
from app.views import account, rhizome as rhizome


def register_router(app):
    app.include_router(account.router, tags=['用户API'])
    app.include_router(rhizome.router, tags=['植物根系'])

