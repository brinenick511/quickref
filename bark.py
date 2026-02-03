import requests
import os
import sys
from pathlib import Path

def barkbark(title="Done", body="Done", num=1):
    body_with_bark = f"{body}?sound=healthnotification"
    bark(title, body_with_bark, num)

def bark(title="Done", body=None, num=1):
    key = os.getenv('BARK_KEY')
    if not key:
        print("Error: BARK_KEY not found", file=sys.stderr)
        return
    num = int(num)
    file_path = os.path.abspath(__file__)
    for i in range(num):
        if num > 1:
            title_with_num = f"{str(title)}_#{i}_{num-1}#"
        else:
            title_with_num = title
        if body:
            url = f"https://api.day.app/{key}/{title_with_num}/{body}"
        else:
            url = f"https://api.day.app/{key}/{title_with_num}"
        try:
            print(f'\n### BARK FROM {file_path} ###\n------\n{url}\n------\n### BARK FROM {file_path} ###\n')
            requests.get(url, timeout=10)
        except Exception as e:
            print(f"Notification failed: {e}", file=sys.stderr)

if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len > 3:
        bark(sys.argv[1], sys.argv[2], sys.argv[3])
    elif arg_len > 2:
        bark(sys.argv[1], sys.argv[2])
    elif arg_len > 1:
        bark(sys.argv[1])
    else:
        bark()