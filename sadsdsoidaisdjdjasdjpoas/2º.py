def per(a,b,c):
    peri = a+b+c
    if a<=(b+c) and b<=(a+c) and c<=(a+b) 
        return peri
    else: 
        return("não é triângulo")

pri = float(input("informe o primeiro lado do triângulo: "))
pri2 = float(input("informe o segundo lado do triângulo: "))
pri3 = float(input("informe o terceiro lado do triângulo: "))
t = per(pri,pri2,pri3)
print("o perímitro de triângulo é: ", t)