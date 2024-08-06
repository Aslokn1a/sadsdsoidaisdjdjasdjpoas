def par(a):
    if a%2!=0:
        return(-1)
    else:
        return(1)

num =int(input("informe um número inteiro: "))
print(par(num))