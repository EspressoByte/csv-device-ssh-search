#!/usr/bin/python3
import os
import re
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
    print(f"Current username: {current_username}")
else:
    print("Unable to determine the current username.")
    exit_program()


def search_lines(lines, patterns):
    matching_lines = []
    for line in lines:
        # Check if the line contains a pattern match for every user input
        if all(re.search(pattern, line, re.IGNORECASE) for pattern in patterns):
            matching_lines.append(line.strip())
    return matching_lines

def main():
    file_path = 'data.txt'
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    while True:
        # Get user input and split it by commas
        user_input = input("Enter search: ")
        
        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            break

        patterns = user_input.split(',')

        # Remove leading and trailing whitespaces from each pattern
        patterns = [pattern.strip() for pattern in patterns]

        # Search for lines that contain a pattern match for every user input
        matching_lines = search_lines(lines, patterns)

        # Output the matching lines
        if matching_lines:
            print("Matching Devices:")
            for match in matching_lines:
                match=match.split(',')
                print(match[0], "-", match[2], "-", match[1])
            if len(matching_lines) == 1:
                print("CONNECTING...", match[1])
                os.system(f"ssh {current_username}@{match[1]}")
        else:
            print("No matching lines found.")

if __name__ == "__main__":
    main()
