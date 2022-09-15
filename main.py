import os

FILE_PATH = input("Insert (.txt) file path: ")


def OpenAndLoadFile():
    with open(FILE_PATH, "r") as file:
        data = file.read()
        dataList = data.split(',')
        if dataList[0] == '2023':
            dataList.pop(0)
        file.close()

        return dataList


def CreateAndUpdateFile():
    content = OpenAndLoadFile()
    counter = 0

    with open('ProxyData_Updated.txt', 'w') as file:
        for i in content:
            file.write('0x' + i)
            if counter < (len(content) - 1):
                file.write(' ')
            counter += 1
        file.close()


if os.path.exists(FILE_PATH) and FILE_PATH.endswith('.txt'):
    OpenAndLoadFile()
    CreateAndUpdateFile()
else:
    print("File does not exist or wrong format!")
