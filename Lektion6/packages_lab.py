'''import math
import cmath
print(math.sin(1))
print(cmath.sin(1))'''

'''from math import sin
from cmath import sin
print(sin(1))'''

'''from cmath import sin
from math import sin
print(sin(1))'''

'''from math import sin
from cmath import sin as csin
print(sin(1))
print(csin(1))'''

import pandas as pd
import numpy as np
numbers = list(input("Enter twelve numbers that will be used to form a dataframe: ")) #skapar en lista med de tolv siffror användaren matar in
list_1 = numbers[0:4] #tar de fyra första siffrorna och lägger i en separat lista
list_2 = numbers[4:8] #tar de fyra mittersta siffrorna och lägger i en separat lista
list_3 = numbers[8:12] #tar de fyra sista siffrorna och lägger i en separat lista
array_1 = np.array(list_1) #omvandlar första listan till en numpy array
array_2 = np.array(list_2) #omvandlar andra listan till en numpy array
array_3 = np.array(list_3) #omvandlar tredje listan till en numpy array
array_final = np.array([array_1, array_2, array_3]) #tar tre olika arrayer och sätter samman till en array
dataset = pd.DataFrame({"Column 1": array_final[:, 0], "Column 2": array_final[:,1], "column 3": array_final[:, 2], "Column 4": array_final[:, 3]}) #skapar en dataframe av datan i array_final
print(dataset) #printar ut den färdiga dataframen




