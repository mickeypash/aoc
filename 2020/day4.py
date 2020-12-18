

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

