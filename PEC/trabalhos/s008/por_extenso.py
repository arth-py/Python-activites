
def separar(num):
    return num%10, num//10%10, num//100%10
   
def unidade(num):
    u, d, c = separar(num)
    if u == 1:return "uma unidade."
    if u == 2:return "duas unidades."
    if u == 3:return "três unidades."
    if u == 4:return "quatro unidades."
    if u == 5:return "cinco unidades."
    if u == 6:return "seis unidades."
    if u == 7:return "sete unidades."
    if u == 8:return "oito unidades."
    if u == 9:return "nove unidades."

def dezena(num):
    u, d, c = separar(num)
    if d == 1:return "uma dezena"   
    if d == 2:return "duas dezenas"   
    if d == 3:return "três dezenas"   
    if d == 4:return "quatro dezenas"   
    if d == 5:return "cinco dezenas"   
    if d == 6:return "seis dezenas"   
    if d == 7:return "sete dezenas"   
    if d == 8:return "oito dezenas"   
    if d == 9:return "nove dezenas" 
   
def centena(num):
    u, d, c = separar(num)
    if c == 1:return "uma centena"
    if c == 2:return "duas centenas"
    if c == 3:return "três centenas"
    if c == 4:return "quatro centenas"
    if c == 5:return "cinco centenas"
    if c == 6:return "seis centenas"
    if c == 7:return "sete centenas"
    if c == 8:return "oito centenas"
    if c == 9:return "nove centenas"

def main():
    num = int(input('Insira o número:\n'))
    u, d, c = separar(num)
    if num > 0 and num < 10:
        print(f"{unidade(num)}")
    elif num > 9 and num < 100:
        if u == 0:
            print(f"{dezena(num)}.")
        else:
            print(f"{dezena(num)} e {unidade(num)}")
    elif num > 99 and num < 1000:
        if u == 0 and d == 0:
            print(f"{centena(num)}.")
        elif u == 0:
            print(f"{centena(num)} e {dezena(num)}.")
        elif d == 0:
            print(f"{centena(num)} e {unidade(num)}")
        else:
            print(f"{centena(num)}, {dezena(num)} e {unidade(num)}")
  
if __name__ == "__main__":
    main()
