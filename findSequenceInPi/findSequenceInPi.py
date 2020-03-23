import time


# making some built in python functions from the ground up
# Guest starring a million digits of Pi


# homemade String find() Method
def subStringSearch(string: str, subString: str):
    checker = ''
    for i in range(0, len(string)):
        if string[i] == subString[0]:
            checker += string[i]
            if i + len(subString) >= len(string):
                pass
            else:
                for j in range(i + 1, i + (len(subString))):
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
    if result == -1:
        print('Not found\n')
    else:
        print(str(substring) + ' is found at the ' + str(result) + ' digit of Pi\n')


# stop_var = -88
# while not str(stop_var).lower() == 'stop':
#     stop_var = input('Enter a number.\nenter "stop" to stop.\n')
#     findInFile(stop_var)


def findSubstringInLargeString():
    substring = '14'
    with open('pi-one-billion.txt', 'r') as file:
        # string = str(file.read()).lower()
        j = 0
        checker = ''
        for stream in file.buffer:
            if char == substring[j]:

                checker += char
                j += 1
                if len(stream) == j:
                    print('big daddy bitch')
                    break
            else:
                checker = ''
                j = 0


with open('pi-one-billion.txt', 'r') as file:
    # string = str(file.read()).lower()
    j = 0
    checker = ''
    place = 5000000
    # print(file.read())
    while file.tell() <= len(file.read()):
        file.seek(place)
        print(file.tell())
        print(file.read(10000000))

        file.seek(place + 500000)
        place += 500000
