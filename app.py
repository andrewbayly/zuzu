from flask import Flask
#from pymongo.mongo_client import MongoClient
#from pymongo.server_api import ServerApi

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

    """
    uri = "mongodb+srv://andrewbayly:AtDyeI6JzqPaTj8n@cluster0.8npn5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    try: 
        client = MongoClient(uri, server_api=ServerApi('1'))
    except Exception as e:
        return(e)
    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        return(e)

    """
    
