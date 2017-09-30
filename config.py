# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sharoon61295:goodmorning15@weeklysoccerquiz.cj7ws5wt0yje.us-east-2.rds.amazonaws.com:3306/weeklySoccerQuiz'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'

questions = [	
	"Who scored a hat-trick last gameweek?",
	"Who are the champions of England? ;)",
	"Who is the manager of Manchester United?",
	"How many penalties were awarded the last gameweek?",
	"Which of these goalkeepers kept a clean sheet last gameweek?"
]

answers = [
	[
		"Alvaro Morata",
		"Romelu Lukaku",
		"Harry Kane",
		"Sergio Aguero"
	],
	[
		"Manchester City FC",
		"Liverpool FC LOL",
		"Manchester United",
		"Chelsea FC",
	],
	[
		"Antonio Conte",
		"Jose Mourinho",
		"Slaven Bilic",
		"Sir Alex Ferguson",
		"Zinedine Zidane"
	],
	[
		"1",
		"2",
		"3",
		"4"
	],
	[
		"Jordan Pickford",
		"Hugo Lloris",
		"Mat Ryan",
		"Asmir Begovic"
	]
]

correctAnswers = [1, 4, 2, 2, 3]