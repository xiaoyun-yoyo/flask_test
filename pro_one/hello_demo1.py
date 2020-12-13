from flask import Flask, render_template
from flask import url_for
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>welcome to my watchlist!!</h1>'


@app.route('/user/<name>')
def user_page(name):
    return 'User page %s' % name


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='tom'))
    print(url_for('user_page', name='sam'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', name=3))




@app.route('/index')
def test_template_test():
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    return render_template('index.html', name=name, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)