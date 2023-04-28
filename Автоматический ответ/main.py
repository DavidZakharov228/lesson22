from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/answer', methods=['GET'])
def answer():
    title = 'Анкета'
    surname = request.form['surname']
    name = request.form['name']
    education = request.form['education']
    profession = request.form['profession']
    sex = request.form['sex']
    motivation = request.form['motivation']
    ready = request.form['ready']
    return render_template('auto_answer.html', title=title, surname=surname, name=name, education=education, profession=profession, sex=sex, motivation=motivation, ready=ready)

@app.route('/auto_answer')
def auto_answer():
    title = 'Автоответ на анкету'
    surname = 'Watny'
    name = 'Mark'
    education = 'выше среднего'
    profession = 'штурман марсохода'
    sex = 'male'
    motivation = 'Всегда мечтал застрять на Марсе!'
    ready = 'True'
    return render_template('auto_answer.html', title=title, surname=surname, name=name, education=education, profession=profession, sex=sex, motivation=motivation, ready=ready)

if __name__ == '__main__':
    app.run(debug=True)