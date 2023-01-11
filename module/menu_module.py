menu = ['', 'Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
price = [0, 1500, 2000, 1700, 2500, 2000, 1900]
bills = [0, 10000, 5000, 1000]
selected_drink = []

# 메뉴 조회
def print_menu():
    for i in range(1, len(price)):
        print("%d. %-10s %5d" % (i, menu[i], price[i]))
    print()

# 음료 선택
def choice_drink():
    drink_num = int(input("음료를 선택해주세요 : "))
    while (drink_num <= 0 or drink_num >= len(menu)):
        drink_num = int(input("해당 메뉴가 존재하지 않습니다.\n음료를 다시 선택해주세요 : "))

    selected_drink.append(menu[drink_num])
    total_price = price[drink_num]
    print("음료 총합 : %d" % (total_price))

    while drink_num != 0:
        drink_num = int(input("추가할 음료를 선택하세요 (결제를 원하시면 0을 입력해주세요) : "))
        if(drink_num >= 1 and drink_num <= len(menu) - 1):
            selected_drink.append(menu[drink_num])
            total_price += price[drink_num]
            print("음료 총합 : %d" % (total_price))
        else:
            if drink_num != 0:
                print("존재하지 않는 메뉴입니다.\n음료를 다시 선택해주세요.")

    return total_price

# 지불 가능한 지폐 조회
def print_biils():
    print("==================================")
    for i in range(1, len(bills)):
        if i == len(bills) -1:
            print("%d. %d원" % (i, bills[i]))
        else:
            print("%d. %d원" % (i, bills[i]), end=" ")
    print("==================================")

# 음료 결제
def drink_payment(total_price):
    print_biils()
    bill = int(input("지불할 지폐를 선택하세요 : "))
    amount = bills[bill]

    while total_price > amount:
        print("결제할 금액 : %d" % total_price)
        print("지불한 금액 : %d" % amount)
        bill = int(input("금액이 부족합니다.\n추가로 지불할 지폐를 다시 선택해주세요 : "))
        amount += bills[bill]

    return amount

def payment_result(total_price, amount):
    print("선택한 메뉴 : ", selected_drink)
    print("음료 총액 : %d" % total_price)
    print("지불한 금액 : %d" % amount)
    print("거스름돈 : %d" % (amount - total_price))


# print_menu()
# total_price = choice_drink()
# amount = drink_payment(total_price)
# payment_result(total_price, amount)