#1:
#for i in range (10):
    #print("Hello and welcome")

#2:
#for a in range (10):
    #print(str(a) * a)

#3:
#secret = int(8)
#while True:
    #user_input = int(input("Enter an integer: "))
    #if user_input > secret:
        #print("It is lower")
    #elif user_input < secret:
        #print("It is higher")
    #elif user_input == secret:
        #print("Correct")
        #break

#4:
#my_list = [10, 20, 33, 40, 50]
#for i in my_list:
    #if i % 2 == 0:
        #print("Even number")
    #else:
        #print("Not allowed")
        #break

#5:
#first_list = [3, 7, 9, 2, 6]
#second_list = [2, 3, 6, 7, 9]
#output = []
#for i in second_list:
    #tup1 = (i, first_list.index(i))
    #output.append(tup1)
#print(output)
    
    
    



#6
#first_list = [3, 7, 9, 2, 6]
#second_list = [2, 3, 6, 7, 9]
#output = [(i, first_list.index(i)) for i in second_list]
#print(output)

#numbers = [1, 2, 3, 4, 5]
#squares = [i+2 for i in numbers]
#print(squares)

#7
#fruits = ["apple", "orange", "pear", "banana", "grapes",]
#basket = []
#x = 0
#y = 0
#fill = int(input("How many fruits do you want?: "))
#for i in range(fill):
    #if x >= 5:
        #x = 0
    #if i <= len(fruits):
        #basket.append(fruits[x])
        #x += 1
    #elif i > len(fruits):
        #basket.append(fruits[x])
        #x += 1

#print(basket)

