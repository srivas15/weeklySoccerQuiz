from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello!</p>\n' 

# EB looks for an 'application' callable by default.
app = Flask(__name__)
application = app

# add a rule for the index page.
app.add_url_rule('/', 'index', (lambda:
    say_hello()))

@app.route('/home')
def home():
    return 'WOW'

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()