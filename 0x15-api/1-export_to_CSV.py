#!/usr/bin/python3
"""Extend to exports to-do list info for a given employee ID to CSV format"""

import csv
import requests
import sys


if __name__ == "__main__":
    # Func that gets the user ID from command-line args given to the script
    user_id = sys.argv[1]

    # It defines the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Script that fetches user information from the API and
    # converts the response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Function that extract the username from the user data
    username = user.get("username")

    # Script fetches the to-do list items associated with the
    # given user ID and convert the response to a JSON object
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Uses the list comprehension to iterate over the to-do list items
    # Writes each item's details (user ID, username, completion status,
    # and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
