n=int(input("Geef een natuurlijk getal: "))
deler=0
for i in range(2,int(n**(1/2)+1)):
    if n%i == 0:
        deler+=1
if deler==0:
    print(n,"is een priemgetal.")
else:
    print(n,"is geen priemgetal.")
