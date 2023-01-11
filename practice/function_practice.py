# 1. 모듈 직접 접근
import module.menu_module

module.menu_module.print_menu()
total_price = module.menu_module.choice_drink()
amount = module.menu_module.drink_payment(total_price)
module.menu_module.payment_result(total_price, amount)

# 2. from을 통한 모듈 접근

from module import menu_module

menu_module.print_menu()
total_price = menu_module.choice_drink()
amount = menu_module.drink_payment(total_price)
menu_module.payment_result(total_price, amount)

# 3. 함수 직접 접근

from module.menu_module import *

print_menu()
total_price = choice_drink()
amount = drink_payment(total_price)
payment_result(total_price, amount)

# 4. __init.py__ 작성 후 모듈 상위 디렉토리 접근
from module import *

menu_module.print_menu()
total_price = menu_module.choice_drink()
amount = menu_module.drink_payment(total_price)
menu_module.payment_result(total_price, amount)