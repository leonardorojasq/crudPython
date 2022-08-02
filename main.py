from fastapi import FastAPI

app = FastAPI(title='API CRUD', description='Api para crear formularios', versions='1.0')


@app.get('/')
def root():
    return "Saludo desde el index"