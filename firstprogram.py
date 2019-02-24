from flask import Flask
app=Flask(__name__)

@app.route("/hello/<int:name>")
def hello(name):
    return "Hello Naman hey naman %d" % name
@app.route("/")
def index():
    return "Index Page!"
if __name__=="__main__":
    app.run()
