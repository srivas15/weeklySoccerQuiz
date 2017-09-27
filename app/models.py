from app import db
'''from flask_login import LoginManager, UserMixin

lm = LoginManager(app)'''

class User(UserMixin, db.Model):
	'''__tablename__ = 'users' '''
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    userName = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.email)

'''@lm.user_loader
def load_user(id):
    return User.query.get(int(id))'''

class Points(db.Model):
	id = db.Column(db.Integer, primary_key=True, db.ForeignKey(User.id))
	points = db.Column(db.Integer)

class GWinfo():
	id = db.Column(db.Integer, primary_key=True, db.ForeignKey(User.id))
	playedThisGW = db.Column(db.Boolean)
	lastQuestionAnswered = db.Column(db.Integer)
	UpdateDtTime = db.Column(db.DateTime)