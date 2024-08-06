def conceito(n):
    if n >= 9:
        return("A")
    elif n>=8:
        return("B")
    elif n>=7:
        return("C")
    elif n>=6:
        return("D")
    else:
        return("F")

nota = float(input("informe a nota do aluno para que o conceito seja atribuído: "))
print(conceito(nota))
     