
def dectohex(dec):
    remain_list = []
    while dec != 0:
        remain = int(dec) % 16
        dec = int(int(dec) / 16)
        remain_list.append(remain)
    return remain_list
        
user_input = input("Decimal :>")
to_convert = dectohex(user_input)
to_convert = to_convert[::-1]


hex_covert = {10 : "A" , 11 : "B" ,12 : "C" , 13 : "D" , 14 : "E" , 15 :"F"}

for i in range(len(to_convert)):
    if to_convert[i] < 10:
        print(i,end='')
    if to_convert[i] >= 10:
        print(hex_covert[to_convert[i]],end='')
