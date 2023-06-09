from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title='FastAPI MongoDB Simple Example',
        docs_url='/api/docs',
    )
    return app
