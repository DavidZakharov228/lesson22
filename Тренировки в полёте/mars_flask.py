from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Тренировки в полёте'

@app.route('/training/врач')
def doctor():
    return render_template('home.html')


@app.route('/training/инженер')
def engineer():
    return render_template('home.html')


@app.route('/training/строитель')
def builder():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
