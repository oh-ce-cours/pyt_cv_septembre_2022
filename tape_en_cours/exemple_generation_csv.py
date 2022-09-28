import typing
import requests

r = requests.get("https://api.github.com/events")


def csv_generator_1(data: typing.List[typing.Tuple[str, str]]):
    with open("api1.csv", "w", encoding="utf8"):
        # print(data)
        for line in data:
            print(line)


datas: typing.List[typing.Tuple[str, str]] = []
for event in r.json():
    datas.append((event["actor"]["display_login"], event["repo"]["name"]))

csv_generator_1(datas)
