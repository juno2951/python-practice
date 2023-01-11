try:
    age = int(input("나이를 입력해주세요 : "))
except:
    print("에러 발생!")
else:
    if age > 19:
        print("성인입니다.")
    else:
        print("미성년자입니다.")