N=int(input("Bir N sayısını giriniz"))
toplam=0
ortalamaçift=0
for i in range(0,N+1):
    if i%2==1:
        toplam = toplam + i
    else:
        ortalamaçift= ortalamaçift+i
ortalama=ortalamaçift/(N)

print("Sum of odd numbers=", toplam)
print("Average of even numbers=", ortalama)

