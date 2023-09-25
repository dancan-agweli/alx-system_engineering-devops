#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

# Import necessary libraries
import requests  # To make HTTP requests
import sys       # To access command-line arguments

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Define the base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Get user information by making a GET request to the API
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    
    # Get the to-do list for the specified user by making a GET request with the user ID as a parameter
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    
    # Create a list of completed tasks from the to-do list
    finished = [t.get('title') for t in todos if t.get('completed') is True]
    
    # Print the summary of completed tasks for the employee
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished), len(todos)))
    
    # Print each completed task
    [print("\t {}".format(c)) for c in finished]

