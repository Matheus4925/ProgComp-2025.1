#Estabelecendo em que número começa e em que número termina.
for n in range(10,100000+1):
    k = 0
    dig = n
    #O while irá pegar cada unidade do número atual.
    while dig != 0:
        r = dig % 10    
        k = 10 * k + r  #Soma das unidades.
        dig = dig // 10
    #Verifica se os números são palíndromos.
    if k == n:
        print(n)
