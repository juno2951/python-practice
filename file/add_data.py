f = open("/usr/local/text/text.txt", 'a')

for i in range(11, 20):
    f.write("{0}번째 데이터입니다.\n".format(i))

f.close()