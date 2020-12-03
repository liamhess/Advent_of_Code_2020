import pytest

with open("input.txt", "r") as file:
    input = file.read().splitlines()

def find(inp):
    for number1 in inp:
        for number2 in inp:
            for number3 in inp:
                common = int(number1) + int(number2) + int(number3)
                # print(common)

                if common == 2020:
                    print(number1 + " - " + number2 + " - " + number3)
                    result = int(number1) * int(number2) * int(number3)
                    return(result)

print(find(input))



def testmethod():
    l = ["1721", "979", "366", "299", "675", "1456"]
    assert find(l) == 241861950