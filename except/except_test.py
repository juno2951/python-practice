try:
    with open("없는 파일", 'r') as f:
        print(f.readline())
except FileNotFoundError as e1:
    pass

    # pass

print("Hello world!")