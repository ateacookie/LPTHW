from flask import Flask
from flask import render_template
from generator1 import Markov

app = Flask(__name__)



@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def generator():
    fairytale = Markov(2)
    fairytale.train('fairytales2.txt')
    output = fairytale.generate(137)

    return render_template('home.html', text=output)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



app.secret_key = '1234567890secret'

if __name__ == "__main__":
    app.run(debug=True)
