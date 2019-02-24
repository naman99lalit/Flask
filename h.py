from flask import Flask, redirect, url_for, request, render_template
app= Flask(__name__)


@app.route('/login', methods =['POST'])
def login():
	if request.method == 'POST':
		user = request.form['naman']
		variable=user
		p=(variable.split())
		return render_template('hello.html',name=p)

@app.route('/login/<item>/hello', methods=['GET', 'POST'])
def hello(item):
	p=item
	return render_template('hellome.html', p=p)

if __name__ == '__main__':
	app.run(debug=True)