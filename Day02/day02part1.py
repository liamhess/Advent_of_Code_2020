import pytest

with open("input.txt", "r") as file:
    input = file.read().splitlines()

with open("testinput.txt", "r") as file:
    test_input = file.read().splitlines()


def solution(input):
    valid_pw_counter = 0

    for i in input:
        amount = i.split(": ")[0].split(" ")[0]
        minimum = int(amount.split("-")[0])
        maximum = int(amount.split("-")[1])
        letter = i.split(": ")[0].split(" ")[1]
        password = i.split(": ")[1]
        # print(amount + ", " + letter + ", " + password)

        if password.count(letter) in range(minimum, maximum+1):
            valid_pw_counter += 1
    
    return valid_pw_counter





def test_solution():
    assert solution(test_input) == 2

print(solution(input))