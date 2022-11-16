def oops():
    raise IndexError

def a():
    try:
        oops()
    except IndexError:
        print("Error")
a()
def oops2():
    raise KeyError

def b():
    try:
        oops2()
    except IndexError:
        print("Index Error")
b()