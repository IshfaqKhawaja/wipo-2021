from fastapi import FastAPI
from PR_EXE import main
app = FastAPI()


@app.get('/fetch')
async def index():
    await main()
    return 'All Data Fetched'
