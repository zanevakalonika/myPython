# import kalender
import calendar

# variable untuk perulangan while
calendar_try = 1
# username input
input_user_name = input('siapakah anda :')
# print data username input
print('hallo,' , input_user_name)
# perulangan while
while calendar_try != 0:
    input_calendar = input('''jawab dengan cara ini (tahun,bulan)\ningin kalender tahun dan bulan berapa :''')
    calendar_output = calendar.month(int(input_calendar[0:4]),int(input_calendar[5:]))
    print(calendar_output)