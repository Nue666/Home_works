def is_constains(*args):
    global calls
    calls += 1
    count = 0
    for i in range(len(args[1])):
        if args[0].lower() == args[1][i].lower():
            print(True)
            break
        else:
            count += 1
    if count == len(args[1]):
        print(False)


def string_info(arg):
    global calls
    calls += 1
    print(tuple([len(arg), arg.upper(), arg.lower()]))


def count_calls():
    print(calls)



calls = 0
string_info(input())
is_constains(input(), ['PascaL', 'pYtHon', 'Java', 'CsS'])
is_constains('Urban', ['ban', 'BaNaN', 'urbAn', 'lohi'])
count_calls()