from flask import Flask, render_template

app = Flask(__name__)

@app.route('/training/<profession>')
def training(profession):
    if 'инженер' in profession.lower() or 'строитель' in profession.lower():
        title = 'Инженерные тренажеры'
        image = 'engineering.jpg'
        layout = 'Схема расположения инженерных тренажеров на космическом корабле'
    else:
        title = 'Научные симуляторы'
        image = 'science.jpg'
        layout = 'Схема расположения научных симуляторов на космическом корабле'

    return render_template('training.html', title=title, image=image, layout=layout)

if __name__ == '__main__':
    app.run(debug=True)