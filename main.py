from fastapi import FastAPI
from PR_EXE import main
app = FastAPI()


@app.get('/fetch/{id}')
async def index():
    print(id)
    await main(id)
    return 'All Data Fetched'
