import pytest

with open("input.txt", "r") as file:
    input = file.read().split("\n\n")

with open("testinput.txt", "r") as file:
    testinput = file.read().split("\n\n")

def solution(input):
    result = 0
    
    for rawGroup in input:
        group = rawGroup.split("\n")
        yesList = list(group[0])


        for person in group:


            for answer in yesList:
                if answer not in person:
                    yesList.remove(answer)



        result += len(yesList)

    return result

def testsolution():
    assert solution(input) == 10

print(solution(input))