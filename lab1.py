a = int(input("Введите число: "))
def get_summa_chisla(a):
    result = []
    while a > 0:
        result.append(a % 10)
        a //= 10
    b = sum(result)
    return b
    print(b)
get_summa_chisla(a) 

