AntalSekunder = int(input("sekunder:"))
AntalDagar = (AntalSekunder-(AntalSekunder % 86400))/86400
print(AntalDagar)
