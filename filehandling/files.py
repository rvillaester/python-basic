import os

def openAndCloseFile(filename):
    f = open(filename, 'w', encoding='utf-8')
    f.close()
#openAndCloseFile('file.txt')

def writeContentToFile(filename):
    with open(filename, 'w') as file:
        file.write('I love python\n')
        file.write('Python is the best')
#writeContentToFile('file.txt')

def readFileContent(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line)
#readFileContent('file.txt')

def appendContentToFile(filename):
    with open(filename, 'a') as file:
        file.write(' Python is easy to learn')
#appendContentToFile('file.txt')

def deleteFile(filename):
    os.remove(filename)
deleteFile('file.txt')