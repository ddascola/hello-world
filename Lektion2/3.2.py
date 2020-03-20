String1 = "jAG tYCKER om äGg"
String2 = "inte"
String3 = "SPAM"
String4 = " "
String1 = String1.title() #Ändrar första bokstaven i varje ord till versal
print(String1)
String1 = String1.swapcase() #Byter gemener mot versaler och vice cersa
print(String1)
String1 = String1.replace("äGG", String3) #Byter ut ordet äGG mot String3
print(String1)
String5 = String1.rsplit(" ", 2) #Delar på andra mellanslaget från höger 
print(String5)
String6 = String5[0] #Plockar ut värden ur String5, som har tre värden. Denna plockar värde 0
print(String6)
String7 = String5[1] #PLockar värde 1
print(String7)
String8 = String5[2] #Plockar värde 2
print(String8)
String2 = String2.title() #Ändrar första bokstaven till versal resten gemener
print(String2)
String2 = String2.swapcase() #Byter plats på gemener och versaler
print(String2)
String9 = String6 + String4 + String2 + String4 + String7 + String4 + String8 
print(String9)









