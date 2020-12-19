import re

FIELDS = ["byr", "iyr", "eyr", "hgt","hcl","ecl","pid"]
def is_valid_passport(passport):
    for attr in FIELDS:
        if attr not in passport.keys():
            return False
    return True

def is_between(_min, field, _max):
    return _min <= int(field) <= _max

def has_digits(field, num):
    return len(field) == num

def is_valid_hgt(passport):
    height = passport["hgt"][:-2] 
    if height.isdigit():
        if "cm" in passport["hgt"]:
            return is_between(150, height, 193)
        if "in" in passport["hgt"]:
            return is_between(59, height, 76)
    return False

def is_valid_passport2(passport):
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
    has_fields = len(passport.keys()) <= 8 or len(passport.keys()) <= 7 and "cid" not in passport.keys()
    if not is_valid_passport(passport): return False

    byr = has_digits(passport["byr"], 4) and is_between(1920, passport["byr"], 2002)
    iyr = has_digits(passport["iyr"], 4) and is_between(2010, passport["iyr"], 2020)
    eyr = has_digits(passport["iyr"], 4) and is_between(2020, passport["iyr"], 2020)
    htg = is_valid_hgt(passport)
    hcl = bool(re.match(r"^#([0-9a-f]{6,})$", passport["hcl"]))
    ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = len(passport["pid"]) == 9 and passport["pid"].isdigit()

    return byr and iyr and eyr and htg and hcl and ecl and pid

with open('input4.txt', 'r') as file:
    lst = file.read().split('\n\n')
    lst = [x.replace('\n', ' ').split() for x in lst]

    passports = [dict(p.split(":") for p in l) for l in lst]

    print(sum([is_valid_passport2(p) for p in passports]))
