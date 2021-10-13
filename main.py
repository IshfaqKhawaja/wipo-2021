from fastapi import FastAPI
from fastapi.responses import FileResponse
from scrape import main
app = FastAPI()


@app.get('/fetch/{id}')
def index(id):
    print(id)
    file = main(id)
    return FileResponse(file)
