# variable untuk perulangan while
menu_main_try = 0
# kata - kata welcome
print('selamat datang di simple calculator')
# perulangan while
while menu_main_try != 1:
    # variable input user 
    angka_pertama = float(input('masukkan angka pertama :'))
    angka_kedua = float(input('masukkan angka kedua :'))
    symbol = input('ketikkan symbol :')
    # kondisi
    if symbol == '+':
        print(angka_pertama + angka_kedua)
    elif symbol == '-':
        print(angka_pertama - angka_kedua)
    elif symbol == '*':
        print(angka_pertama * angka_kedua)
    elif symbol == '/':
        print(angka_pertama / angka_kedua)
    else:
        print('maaf symbol hanya ada + - * / saja')