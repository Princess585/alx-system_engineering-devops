#!/usr/bin/python3
"""
Extend and exports to-do list info for a given employee ID to JSON format

The script takes an employee ID as a command-line arg and exports
that corresponds with user info and to-do list to a JSON file
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Gets the employee ID from the command-line argument
    user_id = sys.argv[1]

    # The base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # It fetches user information using the given employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # It fetches the to-do list for the employee using the given employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Func that creates a dictionary containing the user and to-do list info
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Writes the data to a JSON file with the employee ID as their filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
