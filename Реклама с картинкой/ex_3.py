from flask import Flask, render_template

app = Flask(__name__)



@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


if __name__ == '__main__':
    app.run(debug=True)