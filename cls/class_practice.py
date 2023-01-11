from copy import copy

import menu_class
import special_menu_class

menu1 = menu_class.MenuClass()
menu2 = copy(menu1)
menu3 = menu2

print(id(menu1))
print(id(menu2))
print(id(menu3))

[a,b] = ['python', 'life']
print(a)
print(b)