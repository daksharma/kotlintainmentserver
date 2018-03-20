from flask import Flask

app = Flask(__name__)


def hello():
    return "Hello World! Testing New Python 3.6 Application"


app.add_url_rule('/', view_func=hello)

if __name__ == '__main__':
    app.run()
