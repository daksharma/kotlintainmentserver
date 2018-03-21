from flask import Flask
from flask_graphql import GraphQLView

from network.graphql.schema import schema

app = Flask(__name__)


def graphql_view():
    return GraphQLView.as_view('graphql',
                               schema = schema,
                               graphiql = True)


app.add_url_rule('/graphql', view_func = graphql_view())


def hello():
    return "Hello World!"


app.add_url_rule('/', view_func = hello)

if __name__ == '__main__':
    app.run()
