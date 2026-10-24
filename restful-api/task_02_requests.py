#!/usr/bin/python3
"""Fetch posts from an API and save them to a CSV file."""

import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save selected fields to a CSV file."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        posts_data = []

        for post in posts:
            posts_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(posts_data)
