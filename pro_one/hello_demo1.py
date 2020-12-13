from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)