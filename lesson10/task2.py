def s():
    c = int(input("Enter first number: "))
    d = int(input("Enter second number: "))
    e = c ** 2 / d
    print(e)
    return e


try:
    s()
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero Error")
