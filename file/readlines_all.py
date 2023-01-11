f = open("/usr/local/text/text.txt", 'r')
lines = f.readlines()

for line in lines:
    print(line.strip())

f.close()