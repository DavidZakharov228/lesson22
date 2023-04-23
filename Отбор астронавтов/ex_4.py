from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    surname = request.form['surname']
    name = request.form['name']
    email = request.form['email']
    education = request.form['education']
    profession = request.form['profession']
    gender = request.form['gender']
    motivation = request.form['motivation']
    mars = request.form['mars']

    # сохранение данных в базу данных

    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)
