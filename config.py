import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

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