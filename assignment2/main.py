import os
import re


root_dir = os.getcwd()
file1 = os.path.join(root_dir, "textfile1.txt")
file2 = os.path.join(root_dir, "textfile2.txt")

with open(file1, "r") as file:
    text1 = file.read()

with open(file2, "r") as file:
    text2 = file.read()

numbers1 = re.findall("[0-9]+", text1)
sum1 = sum([int(i) for i in numbers1])

numbers2 = re.findall("[0-9]+", text2)
sum2 = sum([int(i) for i in numbers2])
