from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    user = {'username': 'yURA'}
    return render_template('index.html', user=user)


@app.route('/<int:id>')
def users(id):
    return f'<h1>Ваш порядковый номер {id} </h1>'


@app.route('/<name>')
def people(name):
    return render_template('people.html', name=name)


@app.route('/help/')
def help():
    return '<h1>Мы уже выехали </h1>'


@app.route('/table/')
def t1():
    return render_template('table.html')


if __name__ == '__main__':
    app.run(debug=True)
