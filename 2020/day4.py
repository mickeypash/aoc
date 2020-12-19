ATTRS = ["byr", "iyr", "eyr", "hgt","hcl","ecl","pid"]
def is_valid_passport(passport):
    for attr in ATTRS:
        if attr not in passport.keys():
            return False
    return True

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

with open('input4.txt', 'r') as file:
    lst = file.read().split('\n\n')
    lst = [x.replace('\n', ' ').split() for x in lst]

    passports = [dict(p.split(":") for p in l) for l in lst]
    print(sum([is_valid_passport(p) for p in passports]))
