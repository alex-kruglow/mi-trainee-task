'''The main of mi-trainee-task.'''

from fastapi import FastAPI

from api.v1.secrets import secrets_router

app = FastAPI()
app.include_router(secrets_router)


def main():
    import uvicorn
    uvicorn.run('main:app', reload=True)


if __name__ == '__main__':
    main()
