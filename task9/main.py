from flask import Flask, url_for, request, render_template

app = Flask(__name__)


# @app.route('/answer', methods=['POST', 'GET'])
# @app.route('/auto_asnwer', methods=['POST', 'GET'])
# def form_sample():
#     if request.method == 'GET':
#         return render_template('selection_form.html')
#     elif request.method == 'POST':
#         param = dict()
#         param["title"] = 'Анкета'
#         param["surname"] = request.form['surname']
#         param["name"] = request.form['name']
#         param["education"] = request.form['education']
#         param["profession"] = request.form['prof']
#         param["sex"] = request.form['sex']
#         param["motivation"] = request.form['reason']
#         if request.form.get('accept'):
#             param["ready"] = "True"
#         else:
#             param["ready"] = "False"
#         return render_template('result.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = dict()
    param["title"] = 'Анкета'
    param["name"] = 'Watny'
    param["surname"] = 'Mark'
    param["education"] = 'Выше среднего'
    param["profession"] = 'Штурман Марсохода'
    param["sex"] = 'Male'
    param["motivation"] = 'Всегда мечтал застрять на Марсе!'
    param["ready"] = 'True'
    return render_template('result.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
