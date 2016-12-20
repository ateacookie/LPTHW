from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map1

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map1.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        # The user doesn't have a session...
        # What should your code do in response?
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:

            return render_template('you_died.html')
        else:
            currentscene = map1.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:

                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:

        return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
   session['scene'] = map1.START.urlname
   return redirect(url_for('game_get')) # redirect the browser to the url for game_get




app.secret_key = '\xd0Oi\x9d\x9e\xcd\xfb\xe4\x9f{h\xb8\x89Mo7d\x90\x14\xe6\x95\xc7\xa6|'

if __name__ == "__main__":
    app.run()
