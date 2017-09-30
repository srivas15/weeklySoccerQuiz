#!flask/bin/python
# from app import app


from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return ('WOW')
# print a nice greeting.

# EB looks for an 'application' callable by default.
# application = Flask(__name__)

# add a rule for the index page.
# app.add_url_rule('/', 'index', ("ok"))

# add a rule when the page is accessed with a name appended to the site
# URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
    # header_text + say_hello(username) + home_link + footer_text))

# run the app.
# if __name__ == "__main__":
#     # Setting debug to True enables debug output. This line should be
#     # removed before deploying a production app.
#     application.debug = True
#     application.run()
app.run(debug=True)