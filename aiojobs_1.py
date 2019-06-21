from aiohttp import web
from aiojobs.aiohttp import setup, spawn

async def handler(request):
    await spawn(request, coro())
    return web.Response()

app = web.Application()
app.router.add_get('/', handler)
setup(app)
