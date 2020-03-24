X=1  #Datatyp = Heltal, integer
Y=4
addresses = {"Adam": "Ormvägen 5","Bella": "Klockgatan 1", "Cornelia": "Vikingagatan 3"}  #Datatyp = Dict
cars = ["Volvo", "Opel", "BMW"] #Datatyp = Lista
numbers1 = {1, 2, 3, X, 6} #Datatyp = Set
numbers2 = {Y, 2, 3, 4, 7}
#print(addresses["Bella"])
addresses["Daniel"] = "Prinsgränd 2" #Lägger till värde till "addresses"
#print(len(addresses))
sort = sorted(addresses.keys())[-1]
#print(addresses[sort])
addresses = {v:k for k, v in addresses.items()}
sort2 = sorted(addresses.keys())[0]
#print(addresses[sort2])

#print(cars[X]) #Returnerar andra i ordningen
#print(cars[Y]) #Vill returnera femte i ordningen men finns bara 3 element
#cars.sort() #Sorterar i bokstavsordning
#print(cars[0]) #Printar första bilen i ordningen
cars_2 = cars
cars_3 = cars.copy()
cars.append("Saab")
#print(cars)
#print(cars_2)
#print(cars_3)
cars.append("Volvo")
cars.append("Opel")
cars.append("BMW")
cars.append("Saab")
cars.sort()
cars.reverse()
#print(cars)
#unique_cars = cars
#unique_cars.pop(0)
#unique_cars.pop(1)
#unique_cars.pop(2)
#unique_cars.pop(3)
unique_cars = cars.copy()
unique_cars2 = set(unique_cars)
unique_cars3 = list(unique_cars2)
#print(unique_cars3)

union = numbers1 | numbers2
intersection = numbers1 & numbers2
difference = numbers1 - numbers2
difference2 = numbers2 - numbers1
#print(union) # 1 2 3 4 6 7 
#print(intersection) # 2 3
#print(difference) # 1 6
#print(difference2) # 4 7
