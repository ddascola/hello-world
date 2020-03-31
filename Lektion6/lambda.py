import operator #importerar funktionen operator

operatorlookup = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod} #omvandlar stängtecken till ett ett räknesätt

def input_1():
    number_1 = int(input("Enter first number: ")) #frågar om nummer 1
    number_2 = int(input("Enter second number: ")) #frågar om nummer 2
    arithmetic = input("Choose arithmetic (+, -, /, *, %): ") #frågar om ett specifikt räknesätt
    op = operatorlookup.get(arithmetic) #tar strängen från 'arithmetic' och omvandlar till räknesätt och sparar det i variabeln op
    list_a = [number_1, number_2, op] #sparar number_1 number_2 och op i en lista
    return list_a #returnerar list_a

x = input_1() #sparar outputen från  input_1() i variabeln x


def print_lambda(v1, v2, lambda_f): #definierar funktion som tar 3 argument
    print(f"{v1} och {v2} ger: {lambda_f(v1, v2)}") #resultatet av 'v1' och 'v2' blir 'lambda_f(v1, v2)'

print_lambda(x[0], x[1], x[2]) #kallar på funktionen 'print_lambda' och skickar med argumenten som ligger i variabeln x


    