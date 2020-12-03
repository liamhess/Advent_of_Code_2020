import pytest

with open("input.txt", "r") as file:
    input = file.read().splitlines()

with open("testinput.txt", "r") as file:
    testinput = file.read().splitlines()


line_index = 1
string_index = 1
result = 1


def change_index(right, down):
    global line_index
    global string_index
    line_index += down
    string_index += right

def solution(input, limit, lines, right, down):
    global result
    global line_index
    global string_index
    tree_count = 0
    while True:
        letter = input[line_index-1][string_index-1]
        print(input[line_index-1])
        print(letter)

        if letter == "#":
            tree_count += 1
            print("Baum gefunden: " + str(tree_count))

        print("right: " + str(right) + ", down: " + str(down))

        print("string: " + str(string_index) + ", line: " + str(line_index))
        change_index(right, down)
        print("string: " + str(string_index) + ", line: " + str(line_index) + "\n")

        if string_index > limit:
            print(string_index)
            string_index -= limit
            print(string_index)

        if line_index > lines:
            print(line_index)
            result *= tree_count
            line_index = 1
            string_index = 1
            return tree_count


def testsolution():
    global result
    global line_index
    global string_index
    result = 1
    line_index = 1
    string_index = 1
    solution(testinput, 11, 11, 1, 1)
    solution(testinput, 11, 11, 3, 1)
    solution(testinput, 11, 11, 5, 1)
    solution(testinput, 11, 11, 7, 1)
    solution(testinput, 11, 11, 1, 2)
    assert result == 336


solution(input, 11, 11, 1, 1)
solution(input, 11, 11, 3, 1)
solution(input, 11, 11, 5, 1)
solution(input, 11, 11, 7, 1)
solution(input, 11, 11, 1, 2)

print(result)