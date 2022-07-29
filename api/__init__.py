from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#  Define the Flask app and database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Render the main page
@app.route("/")
def main():
    return """Hi and welcome to <b>Basic GraphQL API for a Bioinformatics Case</b> 
        developed by <a href="http://furkanmtorun.github.io/" target="_blank"><b>@furkanmtorun</b></a>! 
        <br> Please refer to <a href="./graphql"><b>./graphql</b></a> page (endpoint)."""
