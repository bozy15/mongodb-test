import os
import pymongo
from pymongo.message import update

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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# Helper function to find a record by name
def get_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")

    try:
        cursor = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing database")

    if not cursor:
        print("Error! No results found")

    return cursor


# add a new record function
def add_record():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    hair_color = input("Enter hair color: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality,
    }
    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing database")


# show the menu with options in command line
def show_menu():
    print("")
    print("1. Add a new record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


# Find a record by
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


# Edit a record
def edit_record():
    # find a record to edit
    doc = get_record()

    # if record is found, edit it
    if doc:
        update_doc = {}
        print("")
        # loop through the fields and get the user input
        for k, v in doc.items():
            # if the field is not the id, ask for input and update the field in the dictionary
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "]: ")

                # if the user did not enter anything, keep the old value
                if update_doc[k] == "":
                    update_doc[k] = v
        # update the record
        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing database")


# Delete a record
def delete_record():
    doc = get_record()
    # if record is found, delete it variable 
    if doc:
        print("")
        # loop through the fields and get the user input
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        # variable to check if the user wants to delete the record
        confirmation = input("Are you sure you want to delete this record?\n [Y or N] ")
        print("")
        # if the user does want to delete the record, delete it
        if confirmation.lower() == "y":
            try:
                coll.delete_one(doc)
                print("Document deleted")
            except:
                print("Error accessing database")
        # if the user does not want to delete the record, exit the function
        else:
            print("Document not deleted")


# Create, read, update, delete and exit function
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            print("You have selected option 5")
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


# Calls the mongo_connect function above to get a connection object
conn = mongo_connect(MONGO_URI)

# creates a connection to the database
coll = conn[DATABASE][COLLECTION]
# runs the main loop
main_loop()
