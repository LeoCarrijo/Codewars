w = 100
r = 4

def peso(w, r):
    if r == 1:
        return w
    elif r == 0:
        return 0
    epley = w * ( 1 + r / 30)
    McGlothin = 100 * w / 101.3 - 2.67123 * r
    Lombardi = w * r ** 0.10
    lista = [round(epley), round(McGlothin), round(Lombardi)]
    return max(lista)

print(peso(w, r))