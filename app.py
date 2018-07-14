from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis, RedisError
import os
import socket

redis = Redis(host = "redis", db = 0, socket_connect_timeout = 2, socket_timeout = 2)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64))
        email = db.Column(db.String(64))

        def __repr__(self):
                return '<User %r>' % self.username

class UserDetails(db.Model):
	
	id = db.Column(db.Integer, primary_key = True)

	#Aditya is 8, John is 5, Bryan is 7, Steve will be 2
	
	username = db.Column(db.String(64))
	originalMajor = db.Column(db.String(64))
	currentMajor = db.Column(db.String(64))
	homeTown = db.Column(db.String(64))

	def __repr__(self):
		return 'UserDetails %r' % self.username




from flask import Flask, render_template, request

#app = Flask(__name__)




@app.route("/")
def main():
		
	
	return render_template('homePage.html')

@app.route('/initDB', methods = ['POST', 'GEt'])
def initDB():
	
	DBI = None


	if request.method == 'POST':
		DBI = request.form

	#db.create_all()
	
	return render_template('initDB.html')





@app.route('/addUser', methods = ['POST' , 'GET' ])
def addUser():
	if request.method == 'POST':
		newUserData = request.form

	
	newUser = User(id = (newUserData.get('Integer', -1)), username = newUserData.get('username', "NULL"), email = newUserData.get('email', "NULL"))

	currUserName = newUserData.get('username', "NULL")
	print(currUserName)

	db.session.add(newUser)
	db.session.commit()

	


	return render_template("addUser.html", newUserData = newUserData)


@app.route('/addUserDetails', methods = ['POST' , 'GET'])
def addUserDetails():
	

	
	if request.method == 'POST':
		NUDD = request.form


	newUserDetails = UserDetails(id=NUDD.get('Integer' , '-1'),
	username = NUDD.get('username', "NULL"), 
	originalMajor = NUDD.get('originalMajor', "NULL"),
	 currentMajor = NUDD.get('currentMajor', "NULL"),
	 homeTown = NUDD.get('homeTown', "NULL"))
	
	print (newUserDetails.id)
	print(newUserDetails.homeTown)
	print (newUserDetails.username)	
	print(newUserDetails.originalMajor)
	print(newUserDetails.currentMajor)

	db.session.add(newUserDetails)
	db.session.commit()


	return render_template("addUserDetails.html")


#we need to add another webpage that shows both tables joining or something, so when the search query happens, we can access all of the data, thatll be tough



@app.route('/findUserEmail', methods = ['POST' , 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
	
	print(result)
	#UserList = User.query.all()
	#print(UserList)
	key = result.get('Integer', -1)
	print(key)
	desiredUser = User.query.get(key)
	print(desiredUser)
	desiredEmail = None
	UName = desiredUser.username
	if desiredUser is not None:
		desiredEmail = desiredUser.email
	else:
		desiredEmail = "This user does not exist"

	print (desiredEmail)
	#for i in range(0, len(UserList)):
	#	if key == UserList[i].id:
	#		desiredEmail = UserList[i].email
	



	#command to join stuff from first table and stuff from second table

	q = db.session.query(User, UserDetails).filter(User.id == UserDetails.id).filter(User.id == key).filter(UserDetails.id == key).all()
	print(q)
	if not q:
		print("q IS [] ")
		return render_template("accessUserEmail.html", result = result, desiredEmail = desiredEmail)
	

	
	query = q[0][1]
	print(query)

	#this is an inner join 

	return render_template("accessUserEmailAndDetails.html",
		 result = result, desiredEmail = desiredEmail,query = query, UName = UName)


@app.route('/allData', methods = ['POST', 'GET'])
def allUserData():
	

	if request.method == 'POST':
		results = request.form


	
	q = None
	q = db.session.query(User, UserDetails).filter(User.id == UserDetails.id).all()

	print(q)

	#pass the object on, thats all you need, all the work will be done in the html files 

	return render_template("allData.html", q = q)















if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 90)
	

