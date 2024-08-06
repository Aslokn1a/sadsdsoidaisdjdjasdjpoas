def conceito(a,b,c):
    min= a*0.25
    if b<=min and c>=6:
        return("Aprovado")
    else:
        return("Reprovado")
au = int(input("informe o número de aulas do semestre: "))
p = int(input("informe o número de faltas do aluno(a): "))
n = float(input("informe a média do aluno(a): "))

print(conceito(au,p, n))
