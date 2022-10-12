from flask import Flask, render_template, session, redirect, url_for, request
from random import choice

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dhme;kghjanrkael/jgbuilarelkjmgbipuehjmghiotrkjhtoikle'
title = ['Flask', 'Как интересно', 'Ваши предложения', 'Химия', '']
menu = [{'name': 'Главная', 'url': '/'}, {'name': 'Помощь', 'url': 'help'}, {'name': 'О приложении', 'url': 'about'},
        {'name': 'Таблица', 'url': 'table'}, {'name': 'Авторизация', 'url': 'login'}]


@app.route('/index/')
@app.route('/')
def hello():
    user = {'username': 'yURA'}
    return render_template('index.html', user=user, title=choice(title), menu=menu)


@app.route('/help')
def help():
    return render_template('help.html', title='Помощь', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='IT CUB', menu=menu)


# @app.route('/<int:id>')
# def users(id):
#     return f'<h1>Ваш порядковый номер {id} </h1>'


@app.route('/profile/<name>')
def profile(name):
    return render_template('people.html', name=name)


@app.route('/table')
def t1():
    return render_template('table.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


@app.route('/login', methods=["POST", "GET"])
def login():
    print(session)
    if 'user_logged' in session:

        return redirect(url_for('profile', username=session['user_logged']))
    elif request.form['username'] == 'andrei' and request.form['password'] == '123':# and request.method == 'GET':
        session['user_logged'] = request.form['username']
        print(session['user_logged'])
        return redirect(url_for('profile', username=session['user_logged']))
    return render_template('login.html', title="Авторизация")


if __name__ == '__main__':
    app.run(debug=True)
