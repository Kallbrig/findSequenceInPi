
# making some built in python functions from the ground up
# Guest starring a million digits of Pi


# homemade String find() Method
def subStringSearch(string, subString):
    checker = ''
    for i in range(0, len(string)):
        if string[i] == subString[0]:
            checker += string[i]

            for j in range(i + 1, i + len(subString)):
                checker += string[j]
            if checker == subString:
                return i + 1
            else:
                checker = ''

    return -1


def findInFile(substring):
    with open('pi-one-million.txt', 'r') as file:
        f = str(file.read()).lower()
    result = (subStringSearch(f, substring.lower()))
    print(result)



