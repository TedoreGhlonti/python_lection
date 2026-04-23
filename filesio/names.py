

with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())
