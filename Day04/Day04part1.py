import pytest

with open("input.txt", "r") as file:
    rawInput = file.read()

with open("testinput.txt", "r") as file:
    rawTestInput = file.read()


def solution(rawInput):
    validPassports = 0
    input = rawInput.split("\n\n")

    for passport in input:
        if all( ["byr" in passport, "iyr" in passport, "eyr" in passport, "hgt" in passport, "hcl" in passport, "ecl" in passport, "pid" in passport] ):
            validPassports += 1
    
    return validPassports
        
def testSolution():
    assert solution(rawTestInput) == 2

print(solution(rawInput))