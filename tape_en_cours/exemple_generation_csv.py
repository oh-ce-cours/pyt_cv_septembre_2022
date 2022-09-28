import typing
import requests

r = requests.get("https://api.github.com/events")


def csv_generator_1(data: typing.List[typing.Tuple]):
    with open("api1.csv", "w", encoding="utf8"):
        print(data)
        # for line in data:


datas = []
for event in r.json():
    datas.append((event["actor"]["display_login"], event["repo"]["name"]))
