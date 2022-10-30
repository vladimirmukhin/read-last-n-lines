import os

def readLastNLines(file_name, N):
    f = open(file_name, 'r')

    file_size = os.stat(file_name).st_size

    buffer_size = 1
    i           = 1
    lines_read  = 0

    while True:
        f.seek(file_size - buffer_size * i)

        line = f.read()

        if line[0] == '\n' and len(line) != 1:
            lines_read+=1
        if lines_read == N:
            print(line[1:], end='')
            return

        i+=1

if __name__ == '__main__':
    readLastNLines("large.txt", 3)
