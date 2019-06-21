from flask import Flask
from celery import Celery
import time

#broker_url = 'amqp://guest@localhost'  # rabbitmq-as-broker
broker_url = 'mongodb://localhost:27017/test'    #mongodb-as-broker
CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "test",
    "taskmeta_collection": "stock_taskmeta_collection",
}

app = Flask(__name__)
celery = Celery(app.name, broker=broker_url)

@celery.task(bind=True)
def some_long_task(self,id):
    time.sleep(10) #Symbolises long running task1
    print("Done Deal")

@celery.task(bind=True)
def some_long_task_2(self):
    time.sleep(10) #Symbolises long running task2
    print("Done Calculation")

@app.route('/deal/<id>')#Deal Route
def deal(id):
    some_long_task.delay(id)#Function Call
    return ("Deal Made")#Response to server

@app.route('/marginalcalc')#Marginal Calc Route
def marginalcalc():
    some_long_task_2.delay()#Function Call
    return ("Calculation Made")#Response to server

if __name__ == '__main__':
    app.run(debug=True)
