from ariadne import graphql
from ariadne.constants import PLAYGROUND_HTML
from ariadne_graphql_modules import make_executable_schema
from flask import Flask, request, jsonify
from webserver.types import types
from webserver.queries import queries
from webserver.mutations import mutations
from webserver.containers import Application as ApplicationContainer
from webserver.types import User
from webserver import queries as queries_module


print(queries)
schema = make_executable_schema(*types, *queries, *mutations)

app_container = ApplicationContainer()
app_container.wire(modules=[__name__, queries_module])
app = Flask(__name__)
app.container = app_container


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
async def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = await graphql(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)
