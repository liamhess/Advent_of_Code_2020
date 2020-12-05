with open("input.txt", "r") as file:
    input = file.read().splitlines()

with open("testinput.txt", "r") as file:
    testinput = file.read().splitlines()

def solution(input):
    highestID = 0
    for seat in input:
        rowList = range(0, 128)
        columnList = range(0, 8)
        row = 0
        column = 0
        for letter in seat[:7]:
            if letter == "B":
                rowList = rowList[len(rowList)//2:]
            if letter == "F":
                rowList = rowList[:len(rowList)//2]
        row = rowList[0]

        for letter in seat[-3:]:
            if letter == "R":
                columnList = columnList[len(columnList)//2:]
            if letter == "L":
                columnList = columnList[:len(columnList)//2]
        column = columnList[0]

        ID = row * 8 + column
        if ID > highestID:
            highestID = ID
    return highestID

print(solution(input))