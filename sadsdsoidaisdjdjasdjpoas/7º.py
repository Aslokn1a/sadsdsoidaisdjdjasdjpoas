def fat(a):
    f=1
    c=0
    for i in range(a):
        c=c+1
        f=f*c
    return(f)
        
num=int(input("informe um número posítivo: "))
print(fat(num))