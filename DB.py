from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from redis import Redis, RedisError
import os
import socket

redis = Redis(host = "redis", db = 0, socket_connect_timeout = 2, socket_timeout = 2)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#@app.route("/")
#def main():

	#html = "<html> <body> <h2> Database has been initialized </h2> </body> </html>"	

db.create_all()
	#return html






#if __name__ == "__main__":
	#app.run(host = '0.0.0.0', port = 70)
#	app.run()
