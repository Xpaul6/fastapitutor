from fastapi import FastAPI, HTTPException
from data import dick, tools
from models import Tool


app = FastAPI()

@app.get('/')
async def index():
    return {'index':'page'}

@app.get('/get-meme/{meme_id}')
async def get_meme(meme_id: int = None):
    return dick[meme_id]

@app.get('/get-memes') # useless
async def get_memes(number_of_memes: int):
    meme_list = list()
    for i in range(1, number_of_memes + 1):
        meme_list.append(dick[i])
    return meme_list

@app.get('/get-tools-list')
async def get_tools_list():
    return tools

@app.post('/add-tool')
async def add_tool(tool_id: int, tool: Tool):
    if tool_id in tools:
        return {'Error':'baka'}
    tools[tool_id] = tool
    return HTTPException(status_code=200, detail='Success')
