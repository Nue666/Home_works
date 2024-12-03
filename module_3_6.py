def proverka(func, num):
    if num == 0:
        return 0
    else:
        return get_multiplied_digts(num)

def get_multiplied_digts(num):
    str_number = str(num)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digts(int(str_number[1:]))
    elif first == 0:
        return 1
    else:
        return first



result = proverka(get_multiplied_digts(402030), 402030)
result2 = proverka(get_multiplied_digts(30303), 30303)
result3 = proverka(get_multiplied_digts(0), 0)
result4 = proverka(get_multiplied_digts(1), 1)
result5 = proverka(get_multiplied_digts(102030405060708090), 102030405060708090)

print(result)
print(result2)
print(result3)
print(result4)
print(result5)