from fastapi import FastAPI

from api.handlers.users import router as user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='FastAPI MongoDB Simple Example',
        docs_url='/api/docs',
    )
    app.include_router(
        user_router,
        prefix='/api/v1',
    )
    return app
