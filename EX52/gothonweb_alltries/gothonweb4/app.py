from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map2, inventory

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():

	inventory.INV.inventory = []

	if 'scene' in session:
		thescene = map2.SCENES[session['scene']]
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
            # Weird, a POST request to /game with no user input... what should your code do?
			return render_template('you_died.html')
			
		elif "inventory" in str(userinput):
			currentscene = map2.SCENES[session['scene']]
			currentscene.event = inventory.INV.printInventory()
			return render_template('show_scene.html', scene = currentscene)
		
		else:
			currentscene = map2.SCENES[session['scene']]
			nextscene = currentscene.do(userinput)
			print nextscene
			if nextscene is None:
				# There's no transition for that user input.
				# what should your code do in response?
				return render_template('you_died.html')
			elif nextscene[0] is 0:
				currentscene.event = nextscene[1]

				if(nextscene[2] is not None):
					inventory.INV.add(nextscene[2])
				if(nextscene[3] is not None):
					inventory.INV.remove(nextscene[3])

				return render_template('show_scene.html', scene=currentscene)

			elif nextscene[0] is 1:
				if nextscene[2] is None or nextscene[2] in inventory.INV.inventory:
					session['scene'] = nextscene[1].urlname
					currentscene.event = ""
					return render_template('show_scene.html', scene=nextscene[1])
				else:
					currentscene.event = nextscene[3]
					return render_template('show_scene.html', scene=currentscene)
						
	else:
		# There's no session, how could the user get here?
		# What should your code do in response?
		return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
	session['scene'] = map2.START.urlname
	return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = '\xd0Oi\x9d\x9e\xcd\xfb\xe4\x9f{h\xb8\x89Mo7d\x90\x14\xe6\x95\xc7\xa6|'

if __name__ == "__main__":
    app.run()
