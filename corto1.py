
#Funcion para los 3 ultimos numero de carnet
def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            listan.append(num)

        elif num % 2 == 1:
            num = num * 3 + 1
            listan.append(num)

listan = []
n = 832
collatz(n)
print (listan)
