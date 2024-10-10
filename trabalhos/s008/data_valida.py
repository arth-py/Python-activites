 
def separar_data(dma):
    a = dma % 10000
    dma //= 10000
    m = dma % 100
    dma //= 100
    d = dma
    return d, m, a
def validar_data(d,m,a):
    if m < 1 or m > 12:
        return False
    if m == 2:
        if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
            if d < 1 or d > 29:
                return False
        else:
            if d < 1 or d > 28:
                return False
    elif m in [4, 6, 9, 11]:
        if d < 1 or d > 30:
            return False
    else:
        if d < 1 or d > 31:
            return False
    return True
def main():
     
    data = input('Insira a data no formato DDMMAAAA:\n').strip()
    if len(data) != 8:  
        print(False)
    else:
        data = int(data)   
        d, m, a = separar_data(data)   
        validar = validar_data(d, m, a)   
        print(validar)
if __name__ == "__main__":
    main()

