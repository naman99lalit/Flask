from sanic import Sanic,response
import time

app = Sanic()

@app.route('/deal/<id>')
async def deal_func(request,id):
    await asyncio.sleep(10)
    return response.text('Deal Made')

async def process(id):
    asyncio.sleep(10)
    print('Deal Done')

@app.route('/marginalcalc')
async def marginalcalc_func(request):
    resp = await calculation()
    return sanic.response('Calculation Made')

def calculation():
    time.sleep(10)
    print('Calculation Done')

if __name__ == '__main__':
    app.run(workers=2)
