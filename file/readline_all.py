f = open("/usr/local/text/text.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break
    else:
        print(line, end="")

f.close()