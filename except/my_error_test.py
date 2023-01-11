import my_error

def say_nick(nick):
    if nick == "바보":
        raise my_error.MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except my_error.MyError as a:
    print(a)