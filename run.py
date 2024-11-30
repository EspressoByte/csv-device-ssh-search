#!/usr/bin/python3
import os
import csv
import getpass

#collect current user logged into system
def get_current_username():
    try:
        # Use getpass to get the current username
        username = getpass.getuser()
        return username
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get the current username and store it in a variable
current_username = get_current_username()

# Check if the username retrieval was successful
if current_username:
    print(f"Current user: {current_username}")
else:
    print("Unable to determine the current username.")
    exit_program()

userTags=""
username=current_username

while userTags != "exit" and userTags != "q" and userTags != "quit":
    connect=[]
    userTags=input("Enter search tags: ")
    tags=userTags.split(",")
    tags=[x.strip().lower() for x in tags]
#    print(tags)
    if tags[0] == "detailed":
        searchResults="detailed"
        tags.pop(0)
    else:
        searchResults="basic"
    raw_database=open("database.csv")
    read_database=csv.reader(raw_database)
    list_database = list(read_database)
    for device in list_database:
        check =  all(item in device for item in tags)
        if check is True:
            if searchResults == "basic":
                print(device[0], "-",device[1])
                connect.append(device[1])
                #os.system(f"ssh {}username@{device[1]}")
            elif searchResults == "detailed":
                connect.append(device[1])
                print(device)
    if len(connect) == 1:
        os.system(f"ssh {username}@{connect[0]}")

else:
    os.system("clear")
    print("Exiting search program!")

#old data files, last edit a year ago.
