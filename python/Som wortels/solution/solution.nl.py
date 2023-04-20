getal = int(input("Geef een getal"))
som = 0
n = 1
while som < getal:
    if (2*n-1)%3 == 0 or (2*n-1)%5 == 0:
        som += (2*n-1)**(1/2)
    n += 1
print(som)