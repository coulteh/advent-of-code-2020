import re

with open("dec4.txt", "r") as input_file:
    input_data = input_file.read().split("\n\n")


def raw_data_to_dict(data):
    """Pass a list of strings in the format 'key:value key:value' for each list item and return it as a list of dicts instead"""
    return_list = []
    for item in data:
        item_dict = {}
        list_data = item.split()
        for pair in list_data:
            key_value = pair.split(":")
            item_dict[key_value[0]] = key_value[-1]
        return_list.append(item_dict)
    return return_list

def check_validity(passport_data):
    if len(passport_data) < 8:
        return len(passport_data) == 7 and "cid" not in passport_data.keys()
    else:
        return True

def check_fields(passport_data):
    valid = False
    for key in passport_data:
        value = passport_data[key]
        if key == "byr":
            valid = int(value) in range(1920, 2003)
        elif key == "iyr":
            valid = int(value) in range(2010, 2021)
        elif key == "eyr":
            valid = int(value) in range(2020, 2031)
        elif key == "hgt":
            if value[-2:] == "cm":
                valid = int(value[:-2]) in range(150, 194)
            elif value[-2:] == "in":
                valid = int(value[:-2]) in range(59, 77)
            else:
                valid = False
        elif key == "hcl":
            valid = bool(re.match("#(?:[0-9a-f]{6})", value))
        elif key == "ecl":
            valid = value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        elif key == "pid":
            valid = len(value) == 9 and value.isdigit()
        if not valid:
            return valid
    return valid

def check_passports(data):
    passport_list = raw_data_to_dict(data)
    valid_passports = 0
    for passport in passport_list:
        if check_validity(passport):
            if check_fields(passport):
                valid_passports += 1
    return valid_passports


print(check_passports(input_data))
