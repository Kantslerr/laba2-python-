new_posledov = []
a = int(input("Введите минимальное число: "))
def get_less(a):
    x = 20
    posledov = []
    for i in range(x):
        b = int(input("Введите число: "))
        posledov.append(b)
    for i in posledov:
        if a > i:            
            new_posledov.append(i)
    print(new_posledov)
get_less(a)            
