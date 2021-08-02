import os
import pymongo

# if env.py is found, use it to get mongo connection info
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

# create a connection to the mongo server
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# Calls the mongo_connect function above to get a connection object
conn = mongo_connect(MONGO_URI)

# creates a connection to the database
coll = conn[DATABASE][COLLECTION]

# Variable to add new item to the collection
new_docs = [
    {
        "first": "Douglas",
        "last": "Adams",
        "dob": "11/03/1952",
        "gender": "m",
        "hair_color": "Grey",
        "occupation": "Writer",
        "nationality": "british",
    },
    {
        "first": "George",
        "last": "R.R. Martin",
        "dob": "20/09/1948",
        "gender": "m",
        "hair_color": "White",
        "occupation": "Writer",
        "nationality": "American",
    },
]

# Inserts new_item into collection
coll.insert(new_docs)

# Variable to find all items in the collection
documents = coll.find()

# gets a list of all the documents in the collection
for doc in documents:
    print(doc)
