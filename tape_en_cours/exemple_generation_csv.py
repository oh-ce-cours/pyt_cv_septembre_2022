import typing
import requests
import csv


def csv_generator_1(data: typing.List[typing.Tuple[str, str]]):
    with open("api1.csv", "a", encoding="utf8") as csv_file:
        for line in data:
            csv_file.write(",".join(line) + "\n")


def csv_generator_2(data: typing.List[typing.Tuple[str, str]]):
    with open("api1.csv", "a", encoding="utf8") as csv_file:
        for line in data:
            csv_file.write(",".join(line) + "\n")


datas: typing.List[typing.Tuple[str, str]] = []
r = requests.get("https://api.github.com/events")
for event in r.json():
    datas.append((event["actor"]["display_login"], event["repo"]["name"]))

csv_generator_1(datas)
