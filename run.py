#!/usr/bin/python3
import os
import csv
userTags=""
username=""

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
