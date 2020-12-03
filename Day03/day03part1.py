import pytest

with open("input.txt", "r") as file:
    input = file.read().splitlines()

with open("testinput.txt", "r") as file:
    testinput = file.read().splitlines()


line_index = 1
string_index = 1


def change_index():
    global line_index
    global string_index
    line_index += 1
    string_index += 3

def solution(input, limit, lines):
    global line_index
    global string_index
    tree_count = 0
    while True:
        letter = input[line_index-1][string_index-1]
        # print(input[line_index-1])
        # print(letter)
        if letter == "#":
            tree_count += 1
            print("Baum gefunden: " + str(tree_count))
        # print("string: " + str(string_index) + ", line: " + str(line_index))
        change_index()
        # print("string: " + str(string_index) + ", line: " + str(line_index))
        if string_index > limit:
            # print(string_index)
            string_index -= limit
            # print(string_index)
        if line_index > lines:
            # print(line_index)
            return tree_count


def testsolution():
    global line_index
    global string_index
    line_index = 1
    string_index = 1
    assert solution(testinput, 11, 11) == 7

print(solution(input, 31, 323))