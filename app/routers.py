from app.config.settings import setting
from app.views import account, rhizome as rhizome


def register_router(app):
    app.include_router(account.router, prefix='/api', tags=['用户API'])
    app.include_router(rhizome.router, prefix='/api', tags=['植物根系'])

