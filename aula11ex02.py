
lista_pares = []
lista_impares = []
lista_negativos = []

while True:
    print ("Pares: ",lista_pares)
    print ("Impares: ",lista_impares)
    print ("Negativos: ",lista_negativos)

    print("Digite 'sair' para finalizar.")
    teclado =(input(">>> "))

    if teclado == 'sair':
          break
        
    try:
        num = int(teclado)
    except:
        print("Ops, não deu para converter para numero inteiro.")
        continue
    
    if num >= 0: #positivo
        if num % 2 == 0:  #par
            lista_pares.append(num)
        else:
            lista_impares.append(num)
    else:
        lista_negativos.append(num)

    
    
    

