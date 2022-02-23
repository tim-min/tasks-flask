from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def index(sex, age):
    image = "young.jpg" if age < 21 else "notyoung.jpg"
    if sex == "male":
        color = f"({abs((255 - age) // 2)}, {abs((255 - age) // 3)}, {abs(255 - age)})"
    else:
        color = f"({abs(255 - age)}, {abs((255 - age) // 3)}, {abs((255 - age) // 2)})"
    return render_template('ast.html', image=url_for('static', filename=f'images/{image}'), color=color)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
