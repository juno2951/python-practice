f = open("/usr/local/text/text.txt", 'w')
for i in range(1, 11):
    data = "{0}번째 데이터 입니다.\n".format(i)
    f.write(data)
f.close()