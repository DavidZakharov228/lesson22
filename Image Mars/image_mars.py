from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def motto():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def advertising():
    return '''Человечество вырастает из детства.\n
              Человечеству мала одна планета.\n
              Мы сделаем обитаемыми безжизненные пока планеты.\n
              И начнем с Марса!\n
              Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')



if __name__ == '__main__':
    app.run(debug=True)