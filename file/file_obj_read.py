f = open("/usr/local/text/text.txt", 'r')

for line in f:
    print(line.strip())

f.close()