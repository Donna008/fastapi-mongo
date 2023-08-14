from pymongo.mongo_client import MongoClient
import os

# Replace the placeholder with your Atlas connection string
# Create a new client and connect to the server
client = MongoClient('mongodb+srv://ntang800:n1XGgnpR3KxjaNud@cluster0.599tdbt.mongodb.net/students?retryWrites=true&w=majority')
for db_name in client.list_database_names():
    print(db_name)
# Send a ping to confirm a successful connection

client.close()
