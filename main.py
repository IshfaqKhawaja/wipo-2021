from fastapi import FastAPI
from fastapi.responses import FileResponse
from scrape import main
app = FastAPI()


@app.get('/fetch/{id}')
async def index(id):
    print(id)
    file = await main(id)
    return FileResponse(file)
