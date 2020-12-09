
with open("day4.input") as f:
    inputd = f.readlines()

import re

registro = ""
reqs = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
validos = 0
for i, line in enumerate(inputd):
    registro += line
    if line == "\n" or i+1 == len(inputd):
        # process group
        kvals = re.findall(r"(\w+)\:(\#?\w+)", registro )
        if len(reqs.intersection(set([k for k, v in kvals]))) == 7:
            validos += 1
        else:
            print(registro, kvals)
        registro = ""

print(validos)

registro = ""
reqs = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
validos = 0
def checkhgt(inputval):
    suffix = inputval[-2:]
    if suffix == "cm":
        val = int(inputval[:-2])
        if val >= 150 and val <= 193:
            return True
    elif suffix == "in":
        val = int(inputval[:-2])
        if val >= 59 and val <= 76:
            return True
    return False
for i, line in enumerate(inputd):
    registro += line
    if line == "\n" or i+1 == len(inputd):
        # process group
        kvals = re.findall(r"(\w+)\:(\#?\w+)", registro )
        dvals = dict(kvals)
        if len(reqs.intersection(set([k for k, v in kvals]))) == 7:
            dvals["eyr"] = int(dvals["eyr"])
            dvals["iyr"] = int(dvals["iyr"])
            dvals["byr"] = int(dvals["byr"])
            if \
                re.match("^\d{9}$", dvals["pid"]) is not None and \
                dvals["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and \
                re.match("^\#[a-f0-9]{6}$", dvals["hcl"]) is not None and \
                checkhgt(dvals["hgt"]) and \
                dvals["eyr"] >= 2020 and dvals["eyr"] <= 2030 and \
                dvals["iyr"] >= 2010 and dvals["iyr"] <= 2020 and \
                dvals["byr"] >= 1920 and dvals["byr"] <= 2002:
                validos += 1
        registro = ""

print(validos)