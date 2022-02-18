# program kelipatan
kelipatan = [] # - > for remove the last item
kelpt_inf = float(input('kelipatan from? :'))
kelpt_inu = float(input('kelipatan until? :'))
def kelpt_system(bhn):
    while bhn < kelpt_inu:
        bhn += kelpt_inf
        kelipatan.append(bhn)
    if kelipatan[-1] > kelpt_inu:
        kelipatan.pop()

kelpt_system(0)
print(*kelipatan , sep='\n')
print('---------------------------\nand the total :' , len(kelipatan) , 'kelipatan')