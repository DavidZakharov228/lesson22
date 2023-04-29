from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
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
    stay_on_mars = request.form['stay_on_mars']

    # Добавьте код для сохранения данных в базу данных или отправки на почту

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)