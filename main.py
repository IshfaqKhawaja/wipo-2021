from fastapi import FastAPI
from PR_EXE import main
app = FastAPI()


@app.get('/fetch/{num}')
async def index():
    await main(num)
    return 'All Data Fetched'
