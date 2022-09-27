def cat():
    f = open("./fizzbuzz.py", encoding="utf8")
    for line in f.readlines():
        line = line.rstrip()
        print(line)
    f.close()


cat()
