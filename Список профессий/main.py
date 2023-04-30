from flask import Flask, render_template

app = Flask(__name__)


@app.route('c<list_type>')
def list_prof(list_type):
    professions = [
        'инженер-исследователь',
        'пилот',
        'строитель',
        'экзобиолог',
        'врач',
        'инженер по терроформированию',
        'климатолог',
        'специалист по радиоционной защите',
        'астрогеолог',
        'гляциолог',
        'инженер жизнеобеспечивания',
        'метеоролог',
        'оператор марсохода',
        'киберинженер',
        'штурман',
        'пилот дронов'
    ]
    if list_type == 'ol':
        return render_template('ol_list.html', professions=professions)
    elif list_type == 'ul':
        return render_template('ul_list.html', professions=professions)


if __name__ == '__main__':
    app.run()
