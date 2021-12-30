# Input First Question
input_things = input('Anda ingin membeli apa ?')
input_count = input('Berapa harga ' + str(input_things) + ' yang ingin Anda beli ?')
input_jumlah = input('Berapa jumlah ' + str(input_things) + ' yang ingin Anda beli ?')
# Variable Total
total_price = int(input_count) * int(input_jumlah)
# Respon Total
print('Total harga belanjaan ' + str(input_jumlah) + ' ' + str(input_things) + ' yang akan Anda beli adalah ' + str(total_price))
# Input Second Question
input_budget = input('Berapa uang budget yang Anda punya ?')
# Kondisi
if int(input_budget) > int(total_price):
    print('Anda telah membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
    print('Uang Anda tinggal ' + str(int(input_budget) - int(total_price)))
elif int(input_budget) == int(total_price):
    print('Jika Anda membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
    print('Uang Anda tinggal ' + str(int(total_price) - int(input_budget))) 
    input_question = input('Apakah Anda tetap ingin membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' ?')
    if input_question == 'yes' or input_question == 'ya':
        print('Anda telah membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
        print('Uang Anda tinggal ' + str(int(total_price) - int(input_budget))) 
    if input_question == 'no' or input_question == 'tidak':
        print('Anda tidak jadi membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
        print('Uang Anda tetap berjumlah ' + str(input_budget))
if int(input_budget) < int(total_price):
    print('Anda tidak dapat membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
    jumlah_kekurangan = int(total_price) - int(input_budget)
    print('Anda dapat membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price) + ' dengan menambahkan uang budget sejumlah ' + str(jumlah_kekurangan))
    input_questyesno = input('Apakah Anda ingin menambahkan uang budget ?')
    if input_questyesno == 'yes' or input_questyesno == 'ya':
        input_answer = input('Berapa uang budget yang ingin Anda tambahkan ?')
        if int(input_answer) > int(jumlah_kekurangan):
            print('Uang Anda telah cukup untuk membeli ' + str(input_jumlah) + ' ' + str(input_things))
            print('Anda telah membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
            print('Uang Anda tinggal ' + str(int(total_price) - int(input_budget))) 
        elif int(input_answer) == int(jumlah_kekurangan):
            total_budget = int(input_answer) + int(input_budget)
            sisa_uang = int(total_price) - int(total_budget)
            print('Jika Anda membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
            print('Uang Anda tinggal ' + str(sisa_uang))
            input_question = input('Apakah Anda tetap ingin membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' ?')
            if input_question == 'yes' or input_question == 'ya':
                print('Anda telah membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
                print('Uang Anda tinggal ' + str(sisa_uang)) 
            if input_question == 'no' or input_question == 'tidak':
                print('Anda tidak jadi membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
                print('Uang Anda tetap berjumlah ' + str(total_budget))
        if int(input_answer) < int(jumlah_kekurangan):
            total_budget = int(input_answer) + int(input_budget)
            print('Anda tidak dapat membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
            print('Uang Anda tetap berjumlah ' + str(total_budget))
    if input_questyesno == 'no' or input_questyesno == 'tidak':
        print('Anda tidak jadi membeli ' + str(input_jumlah) + ' ' + str(input_things) + ' seharga ' + str(total_price))
        print('Uang Anda tetap berjumlah ' + str(input_budget)) 
