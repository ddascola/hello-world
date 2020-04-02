#1
'''with open('test.txt', 'r') as my_file:
    print(my_file.read())'''

#2
'''with open('test.txt', 'r') as my_file:
    lines = [next(my_file) for line in range(3)]
    print(lines)'''

#3
'''with open('test.txt', 'a') as my_file:
    my_file.write('\n' 'tomater')

with open('test.txt', 'r') as my_file:
    print(my_file.read())'''

#4

#5
'''list_a = []
with open('test.txt', 'r') as my_file:
    for line in my_file:
        list_a.append(line)

print(list_a)'''

#6
'''with open('test.txt', 'r') as my_file:
    var = my_file.read()
    print(var)'''

#7
'''import numpy as np
with open('test.txt', 'r') as my_file:
    #lines = my_file.readlines()
    lines = my_file.read().splitlines()
    array = np.array(lines)
    print(lines)'''

#16
'''my_file = open('test.txt')
print(my_file.closed)
my_file.close()
print(my_file.closed)'''

#17
#se uppgift  nummer 7 (lines = my_file.read().splitlines())

    


        








