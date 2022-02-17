#Ülesanne 5
#Caroline Samarajev
#16.02



#Õpilased
õpilased = ['Juhan','Kati','Maarja','Mario','Mati']




#Nimede lisamine loendisse
nimed = []
for i in range(5):
    nimi = input("sisesta nimed: ")
    nimed.append(nimi)
nimed.sort()
for i in range(len(nimed)):
    print(nimed[i])

