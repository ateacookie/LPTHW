from flask import Flask
from flask import render_template
from generator1 import Markov

#Hack that only works for localhost
# import sys
#
# if sys.version_info.major < 3:
#     reload(sys)
# sys.setdefaultencoding('utf8')

#another option (doesn't work)
# data="UTF-8 DATA"
# udata=data.decode("utf-8")
# asciidata=udata.encode("ascii","ignore")


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def generator():
    fairytale = Markov(2)
    fairytale.train('fairytales2.txt')
    #remove_non_ascii()
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
