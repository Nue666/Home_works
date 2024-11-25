def password(num):
    result = []
    for i in range(1,num+1):
        for j in range(2,num+1):
            if num % (i + j) == 0 and (str(j)+str(i)) not in result and i != j:
                result.append(str(i)+str(j))
    print(f'{num} - число первой вставки\nнужный пароль:')
    print(*result, sep = '')

password(int(input()))
