def readLastNLines(file_name, N):
    f = open(file_name, 'r')
    for line in f.readlines()[-3:]:
        print(line, end='')

if __name__ == '__main__':
    readLastNLines("large.txt", 3)
