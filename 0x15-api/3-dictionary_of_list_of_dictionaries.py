#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    # Define the base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve information about all users (employees) from the API
    users = requests.get(url + "users").json()

    # Open a JSON file for writing
    with open("todo_all_employees.json", "w") as jsonfile:
        # Create a JSON structure containing tasks, completion status, and username for all users
        data = {
            u.get("id"): [
                {
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": u.get("username")
                }
                for t in requests.get(url + "todos", params={"userId": u.get("id")}).json()
            ]
            for u in users
        }
        # Write the JSON data to the file
        json.dump(data, jsonfile)

    # End of the script

