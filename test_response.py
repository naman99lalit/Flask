import traceback
from flask import Flask,request
import time
from werkzeug.wsgi import ClosingIterator

class AfterResponse:
    def __init__(self, app=None):
        self.callbacks = []
        if app:
            self.init_app(app)

    def __call__(self, callback):
        self.callbacks.append(callback)
        return callback

    def init_app(self, app):
        # install extension
        app.after_response = self

        # install middleware
        app.wsgi_app = AfterResponseMiddleware(app.wsgi_app, self)

    def flush(self):
        for fn in self.callbacks:
            try:
                fn()
            except Exception:
                traceback.print_exc()

class AfterResponseMiddleware:
    def __init__(self, application, after_response_ext):
        self.application = application
        self.after_response_ext = after_response_ext

    def __call__(self, environ, after_response):
        iterator = self.application(environ, after_response)
        try:
            return ClosingIterator(iterator, [self.after_response_ext.flush])
        except Exception:
            traceback.print_exc()
            return iterator


app =Flask("after_response")
AfterResponse(app)



rule = request.url_rule
if 'hello/<id>' in rule.rule:
    @app.after_response
    def after_deal(id):
        time.sleep(10)
        print("Deal Done")
elif 'fun' in rule.rule:
    @app.after_response
    def after_deal(id):
        time.sleep(10)
        print("Fun Done")


@app.route("/hello/<id>")
def hello(id):
    after_deal(id)
    return "Hello world!"

@app.route("/fun")
def fun():
    after_deal(1)
    return "Hello Fun"

if __name__ == '__main__':
    app.run(debug=True)
