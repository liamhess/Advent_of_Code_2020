import pytest
import re

with open("input.txt", "r") as file:
    rawInput = file.read()

with open("testinput2.txt", "r") as file:
    rawTestInput = file.read()

def heightChecker(heightString):
    if "cm" in heightString or "in" in heightString:
        unit = heightString[-2:]
        height = int(heightString[:-2])
        if unit == "cm"and height >= 150 and height <= 193:
            return True
        elif unit == "in" and height >= 59 and height <= 76:
            return True
        else:
            return False

def haircolorChecker(haircolorString):
    if "#" in haircolorString and len(haircolorString) == 7 and bool(re.match('^[a-f0-9#]+$', haircolorString)):
        return True
    else:
        return False

def eyecolorChecker(eyecolorString):
    if any( [eyecolorString == "amb", eyecolorString == "blu", eyecolorString == "brn", eyecolorString == "gry", eyecolorString == "grn", eyecolorString == "hzl", eyecolorString == "oth"] ):
        return True
    else:
        return False

def passportidChecker(passportidString):
    if len(passportidString) == 9 and bool(re.match('^[0-9]+$', passportidString)):
        return True
    else:
        return False

def solution(rawInput):
    validPassports = 0
    input = rawInput.split("\n\n")
    passportList = []
    passportDictList = []

    for passport in input:
        if all( ["byr" in passport, "iyr" in passport, "eyr" in passport, "hgt" in passport, "hcl" in passport, "ecl" in passport, "pid" in passport] ):
            passportList.append(passport)

    passportListFormatted = [passport.replace("\n", " ") for passport in passportList]

    for passport in passportListFormatted:
        dict = {}
        passportFields = passport.split(" ")
        for passportField in passportFields:
            dict[passportField.split(":")[0]] = passportField.split(":")[1]
        passportDictList.append(dict)
    
    for passport in passportDictList:
        if all  ( [ int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002,
                int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020,
                int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030,
                heightChecker(passport["hgt"]),
                haircolorChecker(passport["hcl"]),
                eyecolorChecker(passport["ecl"]),
                passportidChecker(passport["pid"])] ):
            validPassports += 1
    return validPassports


def testSolution():
    assert solution(rawTestInput) == 4

print(solution(rawInput))