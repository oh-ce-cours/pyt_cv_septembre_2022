import requests

r = requests.get("https://api.github.com/events")
for event in r.json():
    print(f'{event["actor"]["display_login"]} sur le dépot {event["repo"]["name"]}')
