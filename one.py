import os

def readLastNLines(file_name, N):
    os.system(f"tail -{N} {file_name}")

if __name__ == '__main__':
    readLastNLines("file.txt", 3)
