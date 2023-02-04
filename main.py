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

@app.get('/get-memes')
async def get_memes(number_of_memes: int):
    meme_list = list()
    for i in range(1, number_of_memes + 1):
        meme_list.append(dick[i])
    return meme_list
