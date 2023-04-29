from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
def answer():
    data = {
        'surname': 'Mark',
        'name': 'Jane',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', data=data)


@app.route('/auto_answer')
def auto_answer():
    data = {
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', data=data)


if __name__ == '__main__':
    app.run()
