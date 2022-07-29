from ariadne import (
    QueryType,
    ObjectType,
    graphql_sync,
    load_schema_from_path,
    make_executable_schema,
)
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request

from api import app
from api.resolvers import resolve_genes, resolve_transcripts, resolve_expression_profiles

# Set Query, Object (later Mutation type can come here) and their resolvers
query = QueryType()
gene = ObjectType("Gene")
transcript = ObjectType("Transcript")
query.set_field("genes", resolve_genes)
query.set_field("transcripts", resolve_transcripts)
query.set_field("expression_profiles", resolve_expression_profiles)

# Set objects and their resolvers for nested queries
gene.set_field("transcripts", resolve_transcripts)
transcript.set_field("expression_profiles", resolve_expression_profiles)

# List of all bindables
bindables = [query, gene, transcript]

# Set GraphQL Schema
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, bindables)

# Run GrahpQL UI
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


# Run GrahpQL Server
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
    status_code = 200 if success else 400
    return jsonify(result), status_code


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
