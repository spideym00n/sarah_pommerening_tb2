import streamlit as st
from pymongo.mongo_client import MongoClient
from datetime import datetime

user = st.secrets['user']
mongodb_password = st.secrets['mongodb_password']
# MongoDB Connection Setup
@st.cache_resource
def connect_to_mongo():
    user = st.secrets["user"]
    db_password = st.secrets["mongodb_password"]

    uri = f"mongodb+srv://{user}:{db_password}@tb2.rjdw7.mongodb.net/?retryWrites=true&w=majority&appName=TB2"

    client = MongoClient(uri)

    return client

# Add a new message
def add_message(username, message):
    db = connect_to_mongo()
    advice_collection = db.get_collection["advice_board"]
    advice_collection.insert_one({
        "username": username,
        "message": message,
        "timestamp": datetime.now()
    })

# Retrieve all messages
def get_all_messages():
    db = connect_to_mongo()
    advice_collection = db.get_collection["advice_board"]
    return list(advice_collection.find().sort("timestamp", -1))
