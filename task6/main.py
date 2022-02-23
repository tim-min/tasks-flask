from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/distribution')
def index():
    astronauts = ["Гриша", "Леша", "Петя", "Тедди", "Евгений", "Брахматра"]
    return render_template('list.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
