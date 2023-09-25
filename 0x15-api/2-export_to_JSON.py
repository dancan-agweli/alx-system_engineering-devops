#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

# Import necessary libraries
import json
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command-line arguments
    u_id = sys.argv[1]

    # Define the base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information by making a GET request to the API
    user = requests.get(url + "users/{}".format(u_id)).json()

    # Get the username from the user information
    username = user.get("username")

    # Get the to-do list for the specified user by making a GET request with the user ID as a parameter
    todos = requests.get(url + "todos", params={"userId": u_id}).json()

    # Open a JSON file for writing
    with open("{}.json".format(u_id), "w") as jsonfile:
        # Create a JSON structure containing user ID, username, tasks, and completion status
        data = {
            u_id: [
                {"task": t.get("title"), "completed": t.get("completed"), "username": username}
                for t in todos
            ]
        }
        # Write the JSON data to the file
        json.dump(data, jsonfile)

    # End of the script

