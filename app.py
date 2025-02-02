from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

"""
@app.route('/')
def hello_world():
    #return "Hello World!"

    uri = "mongodb+srv://andrewbayly:AtDyeI6JzqPaTj8n@cluster0.8npn5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    try: 
        client = MongoClient(uri, server_api=ServerApi('1'))
        #return("client created")
    except Exception as e:
        return(e)

    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        return(e)

from flask import Flask 
from flask import render_template 
  
# creates a Flask application 
app = Flask(__name__) 
"""  

@socketio.on('message')
def handle_message(data):
    send(data)
    #print('received message: ' + data)
  
@app.route("/") 
def hello(): 
    #message = "Hello, World"
    return render_template('index.html') 

# run the application 
if __name__ == "__main__": 
    #app.run(debug=True)
    socketio.run(app)
