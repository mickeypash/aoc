
"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
"""
ATTRS = ["byr", "iyr", "eyr", "hgt","hcl","ecl","pid","cid"]
def search(line):
    query = {i:False for i in ATTRS}

    tokens = line.split(" ")
    for token in tokens:
        key, value = token.split(":")
        if key in query.keys():
            query[key] = True
    return query

f = open("input4.txt")

lines = f.read()

test = []
for line in lines.split("\n")[:5]:

    if line == "":
        continue
    else:
        print(search(line))
        test.append(line)

print(test)

f.close()
"""
import json

ATTRS = ["byr", "iyr", "eyr", "hgt","hcl","ecl","pid"]
def is_valid_passport(passport):
    for attr in ATTRS:
        if attr not in passport.keys():
            return False
    return True

with open('input4.txt', 'r') as file:
    lst = file.read().split('\n\n')
    lst = [x.replace('\n', ' ').split() for x in lst]

    valid_passports = []

    for l in lst:
        passport = {}
        for p in l:
            key, value = p.split(":")
            passport[key] = value
        valid_passports.append(is_valid_passport(passport))

    print(sum(valid_passports))

