from colorama import Fore, Back, Style
# Fore - задає колір тексту в консолі
print(Fore.RED + "Red text")
print("some text")
# Back - задає задній колір
print(Back.GREEN + "Green text")
print("some text")
print(Back.BLUE + "Blue text")
# Style.DIM
print(Style.DIM + "Dim text")
# Style.RESET_ALL - скидає всі налаштування
print(Style.RESET_ALL)
print("some text")