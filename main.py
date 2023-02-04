from fastapi import FastAPI

dick = {
    1:'bruh',
    2:'lol',
    3:'lmao',
    4:'cringe'
}

app = FastAPI()

@app.get('/')
async def index():
    return {'index':'page'}

@app.get('/get-meme')
async def get_meme(meme_id: int = None):
    return dick[meme_id]

