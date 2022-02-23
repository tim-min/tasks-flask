from flask import Flask, request, render_template, redirect, url_for
import json
from random import choice
from pprint import pprint

app = Flask(__name__)


def get_astronaut():
    with open("templates/astronauts.json", encoding="utf-8") as file:
        data = json.load(file)
    result = list()
    for key, values in data.items():
        result.append(values)
    return choice(result)


@app.route('/table')
def index():
    astronaut = get_astronaut()
    astronaut["profs"] = ", ".join(sorted(astronaut["profs"]))
    return render_template('ast.html', **astronaut)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
