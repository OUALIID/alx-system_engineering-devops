#!/usr/bin/python3
"""Export data in CSV format."""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    id = int(sys.argv[1])
    user_request = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}")
    user = user_request.json()["username"]

    tasks_request = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={id}")

    filename = "2.csv"
    for task in tasks_request.json():
        if task['userId']:
            data = [
                    str(id),
                    str(user),
                    str(task["completed"]),
                    str(task["title"]),
                ]
            with open(filename, mode="a") as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                writer.writerow(data)
