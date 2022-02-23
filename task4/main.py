from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def form_sample(prof):
    image = ""
    if "инженер" in prof.lower():
        image = "ing.jpg"
    elif "строитель" in prof.lower():
        image = "bldr.jpg"
    elif "врач" in prof.lower():
        image = "md.jpg"
    else:
        image = "othr.jpg"
    return render_template('training.html', image=image)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
