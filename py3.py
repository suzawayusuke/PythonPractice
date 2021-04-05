def hello():
    return "ごぶさた！"

def dec(func):
    def new_func():
        print('function called:' + func.__name__)
        return func()
    return new_func

hello = dec(hello)

print(hello())
