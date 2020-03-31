import operator

operatorlookup = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod}

def input_1():
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    arithmetic = input("Choose arithmetic (+, -, /, *, %): ")
    op = operatorlookup.get(arithmetic)
    list_a = [number_1, number_2, op]
    return list_a

x = input_1()


def print_lambda(v1, v2, lambda_f):
    print(f"{v1} och {v2} ger: {lambda_f(v1, v2)}")

print_lambda(x[0], x[1], x[2])


    