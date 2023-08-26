#!/usr/bin/env python3

import os
import requests

path = "/data/feedback/"
def get_files():
    txt_files = [f for f in os.listdir(path)]
    return txt_files

def process_txt(txt_files):
    content = {}
    for file in txt_files:
        with open(os.path.join(path, file), "r", encoding="UTF-8") as f:
            content["title"] = f.readline().strip()
            content["name"] = f.readline().strip()
            content["date"] = f.readline().strip()
            content["feedback"] = f.readline().strip()
        response = requests.post("http://<corpweb external ip>/feedback/", data=c>
        if response.ok:
            print("loaded entry")
        else:
            print(f"load entry error: {response.status_code}")

if __name__ == "__main__":
    txt_files = get_files()
    process_txt(txt_files)
