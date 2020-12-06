import pytest

with open("input.txt", "r") as file:
    input = file.read().split("\n\n")

with open("testinput.txt", "r") as file:
    testinput = file.read().split("\n\n")

def solution(input):
    result = 0
    for group in input:
        formattedGroup = list(group.replace("\n", ""))
        noDuplicateGroup = list(dict.fromkeys(formattedGroup))
        result += len(noDuplicateGroup)
    return result

def testsolution():
    assert solution(testinput) == 11

print(solution(input))