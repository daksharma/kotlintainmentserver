from flask import Flask
from flask_graphql import GraphQLView

from graphql.schema import schema

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.router('/graphql')
def graphql_view():
    return GraphQLView.as_view('graphql',
                               schema = schema,
                               graphiql = True)


if __name__ == '__main__':
    app.run()
