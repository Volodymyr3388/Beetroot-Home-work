# Task 3

def make_operations(operation, *args):
    if operation == "+":
        result = 0
        for num in args:
            result += num
        return result

    elif operation == "*":
        result = 1
        for num in args:
            result *= num
        return result

    elif operation == "-":
        result, *rest = args
        for num in rest:
            result -= num
        return result


print(make_operations("+", 5, 5, -10, -20))
print(make_operations("*", 5, 5, -10, -20))
print(make_operations("-", 5, 5, -10, -20))