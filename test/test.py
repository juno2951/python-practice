# 1. 리스트 컴프리헨션 적용 전
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)
# 결과

# 2. 리스트 컴프리헨션 적용 후
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)