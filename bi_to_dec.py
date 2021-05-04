binary = input("Please Enter Your Binary ::> ")

def bi_to_deci(bi):
    length_of_bi = len(bi)
    deci_array = []
    deci_value = []
    for i in range(length_of_bi):
        deci_array.append(2**i)
    # print(deci_array)
    rev_bi = bi[::-1]
    irr = 0
    value = 0
    for i in rev_bi:
        if i == "1":
            deci_value.append(deci_array[irr])
            irr += 1
            # print(1)
        else:
            irr += 1
            # print(0)
    # print(deci_value)
    for i in range(len(deci_value)):
        value += deci_value[i]
        # print(i," <<< ")
    return value

deci = bi_to_deci(binary)
print("The Decimal Value is ::> " ,deci)