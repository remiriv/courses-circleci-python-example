import os
from flask import Blueprint, render_template

app = Blueprint("app", __name__)


def get_environment_name():
    return os.getenv("ENV_NAME") or "default"


@app.route("/env", methods=["GET"])
def get_environment():
    environment_name = get_environment_name()

    return render_template("index.html", environment_name=environment_name)
