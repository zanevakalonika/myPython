print('welcome to the uler piton todo list :)')
daily_list = []
if len(daily_list) == 0:
    quest_list = int(input('total daily list that you want :'))
    for e in range(0 , quest_list):
        add_list = input('input your daily list :')
        daily_list.append(add_list)
        print(*daily_list , sep='\n')
        print()
print('total list :' , len(daily_list) , '\n--------------------\nmenu :\n1. delete all lists\n2. delete the list by type the list number\n3. add list')
while True:
    try:
        choosing_menu = int(input('type number from menu option :'))
    except ValueError:
        print('please type a number!!')
        continue
    if choosing_menu == 1:
        quest_1 = input('want to delete all your lists (yes or no)? :')
        if quest_1 == 'yes':
            daily_list.clear()
            print('now, your total list is' , len(daily_list) , '\nthank you for using the uler piton todo list :)')
            quit()
        if quest_1 == 'no':
            print('ok' , '\nnow, your total list is still' , len(daily_list))
            continue
        else:
            print('please type yes or no!!')
    if choosing_menu == 2:
        if len(daily_list) > 1:
            quest_removelist = int(input('list number do you want to delete :'))
            daily_list.remove(daily_list[quest_removelist - 1])
            print('your total list is' , len(daily_list))
            print(*daily_list , sep='\n')
        else:
            print('type number 1 in question \'type number from menu option :\' to delete your daily list')
            continue
    if choosing_menu == 3:
        try:
            quest_list_add = int(input('total daily list you want to add :'))
        except ValueError:
            print('please type a number!!')
            continue
        for i in range(0 , quest_list_add):
            add_list_ag = input('input your daily list :')
            daily_list.append(add_list_ag)
            print(*daily_list , sep='\n')
            print('------------------------------------------' , '\nnow, your total list is' , len(daily_list))
            print()