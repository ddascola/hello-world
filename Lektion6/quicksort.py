def quicksort(unsorted_list):
    p = unsorted_list.pop() #tar ut en pivot och kallar den p
    smaller = [] #tom lista 'smaller'
    larger = [] #tom lista 'larger
    for element in unsorted_list: #loopar genom varje element i unsorted_list
        if element == p: continue #ska ej gå igenom 'p' i loopen
        elif element <= p: #kollar om element är mindre/lika med 'pä
            smaller.append(element) #om ovan stämmer, lägg elementet i 'smaller'
        else:                     #om satsen ovan ej stämmer, alltså element är större än 'p', lägg element i 'larger'
            larger.append(element) 
    
    if len(smaller) > 1: #kollar om 'smaller' har mer än ett element
        smaller.sort() #sorterar 'smaller'
    
    if len(larger) > 1: #kollar om 'larger' har mer än ett element
        larger.sort()  #sorterar 'larger'

    sorted_list = [(smaller) + [p] + (larger)] #skapar sammansatt lista av 'smaller', 'p' och 'larger'
    return sorted_list                         #returnerar sorterade listan
print(quicksort([2,5,7,3,4,8,9,6,3,1,4,3,6,8,7,5,4,3]))
    





