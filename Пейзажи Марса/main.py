from flask import Flask, render_template

app = Flask(__name__)

@app.route('/carousel')
def carousel():
    return render_template('carousel.html')

if __name__ == '__main__':
    app.run(debug=True)