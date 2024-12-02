def is_constains(*args):
    count_calls()
    count = 0
    for i in range(len(args[1])):
        if args[0].lower() == args[1][i].lower():
            return True
            break
        else:
            count += 1
    if count == len(args[1]):
        return False

def string_info(arg):
    count_calls()
    return tuple([len(arg), arg.upper(), arg.lower()])



def count_calls():
    global calls
    calls += 1


calls = 0
print(string_info(input()))
print(is_constains(input(), ['PascaL', 'pYtHon', 'Java', 'CsS']))
print(is_constains('Urban', ['ban', 'BaNaN', 'urbAn', 'lohi']))
print(calls)