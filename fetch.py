import requests
import time 
import files
import os
import json

def fetch_repo_data():
    repo_url = input("Enter Your (PUBLIC) Repo URL (no strings) (https://api.github.com/repos/user_name/repo_name): ")
    time.sleep(2)
    response = requests.get(repo_url, timeout=5)
    response.raise_for_status()
    return response.json()

def auth():
    res = fetch_repo_data()     
    files.write_github_file(res)
    print(f"1.ID: {res['id']}")
    print(f"2.Repo Name: {res['name']}")
    print(f"3.Owner Name: {res['owner']['login']}")
    print(f"4.language: {res['language']}")
    print(f"5.Description: {res['description']}")
    print(f"6.URL: {res['html_url']}")
    print(f"7.Stars: {res['stargazers_count']}")
    print(f"8.Forks: {res['forks_count']}")
    print(f"9.Watchers: {res['watchers_count']}")