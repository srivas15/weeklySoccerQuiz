from app import app

# EB looks for an 'application' callable by default.
application = app

# @app.route('/')
# @app.route('/index')
# def home():
#     return 'WOW'

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()