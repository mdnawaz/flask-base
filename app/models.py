from app import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(128))
	body = db.Column(db.Text)

	def __init__(self, title, body):
		self.title = title
		self.body = body
		
class Users(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(128))
	password = db.Column(db.String(128))

	def __init__(self, name, password):
		self.name = name
		self.password = password
		
