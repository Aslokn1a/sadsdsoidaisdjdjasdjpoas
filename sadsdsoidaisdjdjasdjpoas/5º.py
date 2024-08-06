def classe_eleitoral(a):
    if a<16:
        return("Não-eleitor")
    elif a>=16 and a<18 and a<=65:
        return("Eleitor facultativo")
    else:
        return("Eleitor Obrigatório")

idade = int(input("informe a idade do ser humano: "))
print(classe_eleitoral(idade))