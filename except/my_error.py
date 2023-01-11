class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."