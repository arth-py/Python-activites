
def morango_preco(mor):
    preco =  mor * 2.50 if mor <= 5 else mor * 2.20
    return preco
def maca_preco(maca):
    preco = maca * 1.80 if maca <= 5 else maca * 1.50 
    return preco 
def main():
    
    morango = float(input('Insira o valor do morango:\n'))
    maca = float(input('Insira o valor da maçã:\n'))
    p_morango = morango_preco(morango)
    p_maca = maca_preco(maca)
    f_total = morango + maca
    p_total = p_morango + p_maca
    if f_total > 8 or p_total > 25:
        p_total -= p_total * (10/100)
        print(f"Valor total:\nR${p_total:.2f}")
    else:
        print(f"Valor total:\n R$ {p_total:.2f}")

if __name__ == "__main__":
    main()
