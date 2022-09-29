from flask import Flask, render_template
from random import choice

app = Flask(__name__)
title = ['Flask', 'Как интересно', 'Ваши предложения', 'Химия', '']
menu = [{'name': 'Главная', 'url': '/'}, {'name': 'Помощь', 'url': 'help'}, {'name': 'О приложении', 'url': 'about'}]


@app.route('/index/')
@app.route('/')
def hello():
    user = {'username': 'yURA'}
    return render_template('index.html', user=user, title=choice(title), menu=menu)


@app.route('/help')
def help():
    return render_template('help.html', title=title)


@app.route('/about')
def about():
    return render_template('about.html', title=title)


@app.route('/<int:id>')
def users(id):
    return f'<h1>Ваш порядковый номер {id} </h1>'


@app.route('/<name>')
def people(name):
    return render_template('people.html', name=name)


@app.route('/table/')
def t1():
    return render_template('table.html')


if __name__ == '__main__':
    app.run(debug=True)
