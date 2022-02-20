import os
import json


def alphabet():
    if not os.path.isdir("alphabet"):
        os.mkdir("alphabet")
        os.chdir("alphabet")
    for i in range(97, 123):
        with open(chr(i), "w") as file:
            file.write(chr(i))


def three_fail(file1, file2):
    with open("file1", ) as f:
        k = f.readlines()
    with open("file2", ) as f1:
        k1 = f1.readlines()
    with open("three_file.txt", "w") as f2:
        for i in range(len(k)):
            f2.write(k[i] + k1[i])


def numb_word(file):
    with open("file") as file_1:
        ln = {}
        for i in file_1:
            ln[f"{i}"] = len(i.split())
        f2 = json.dumps(ln, indent=3)
    return f2






