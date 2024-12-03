def get_multiplied_digts(func, num):
    if num == 0:
        return 0
    else:
        return get_multiplied_digt(num)

def get_multiplied_digt(num):
    str_number = str(num)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digt(int(str_number[1:]))
    elif first == 0:
        return 1
    else:
        return first



result = get_multiplied_digts(get_multiplied_digt(402030), 402030)
result2 = get_multiplied_digts(get_multiplied_digt(30303), 30303)
result3 = get_multiplied_digts(get_multiplied_digt(0), 0)
result4 = get_multiplied_digts(get_multiplied_digt(1), 1)
result5 = get_multiplied_digts(get_multiplied_digt(102030405060708090), 102030405060708090)

print(result)
print(result2)
print(result3)
print(result4)
print(result5)