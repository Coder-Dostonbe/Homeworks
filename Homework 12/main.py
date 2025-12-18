import requests
import json
from pprint import pprint

posts = requests.get("https://jsonplaceholder.typicode.com/posts/")
alter = posts.json()
pprint(posts)

json_data = []

for post in alter:
    user_id = post["userId"]
    id1 = post["id"]
    title = post["title"]
    body = post["body"]

    json_data.append({
        "Foydalanuvchi idsi": user_id,
        "Id": id1,
        "Mavzu": title,
        "Tana": body
    })
with open("posts.txt", mode="w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
