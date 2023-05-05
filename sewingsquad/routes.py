# Imports
from flask import render_template
from sewingsquad import app, db


@app.route("/")
def main_page():
    return render_template("base.html")
