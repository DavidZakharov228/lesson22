from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        astronaut_id = request.form['astronaut_id']
        astronaut_password = request.form['astronaut_password']
        capitan_id = request.form['capitan_id']
        capitan_password = request.form['capitan_password']
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()