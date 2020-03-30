#1.3.1 utan funktioner
#number = int(input("Enter a number: "))
#five = 5
#if number <= five:
    #for i in range (number):
        #print(str(i) * i)
#elif number > five:
        #print(str(number) * number)

#1.3.2 med funktioner
def multiply_string_integer(argument1):
    convert = str(argument1)
    x = str(convert) * argument1
    print("Svar: " + x)
    

#number = int(input("Enter a number: "))
#five = 5
#if number <= five:
    #for i in range (number):
        #print(str(i) * i)
#elif number > five:
        #multiply_string_integer(number)

#2.3

#number = int(input("Enter a number: "))
#five = 5
#x = str(number) * number
#if number <= five:
    #for i in range (number):
        #y = str(i) * i
        #print("Svar: " + y)
#elif number > five:
    #print("Svar: " + x)



number = int(input("Enter a number: "))
five = 5
if number <= five:
    for i in range (number):
        print(str(i) * i)
elif number > five:
        multiply_string_integer(number)

#3





