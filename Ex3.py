def area(base,altura):
    return print('A área do triângulo é : ',base * altura)

def primo(num):
    primo = True
    for i in range(2,num):
        if (num % i == 0) and (num > 1):
            primo = False 
            print("O valor de :",num,"mod",i," == ",num%1)
            return print("O número não é primo ! ")
            break
    if primo == True and num != 1 :
        print("O numero é primo ! ")

def somaVetor(vetor):
    somaVet = 0
    for i in vetor:
        if i % 2 == 0:
            somaVet += i
    return print('A soma dos elementos pares no vetor é : ',somaVet)

def Escolha():
    choose = int(input("Escolha o programa a ser executado : \n1.Calculo de área de um retangulo \n2.Determinar Número primo \n3.Calcular soma dos elementos pares de um vetor \n"))
    if choose == 1 : #Calculo da área do triangulo
        base = int(input("Digite os valores de base do triângulo : "))
        altura = int(input("Digite os valores de altura do triângulo : "))      
        area(base,altura)

    elif choose == 2: #Verificar se é primo ! 
        numero = int(input("Digite o valor para verificar se é primo ! "))
        primo(numero)

    elif choose == 3: #Soma dos valores pares do vetor !
        vetor = []
        while len(vetor) != 50:
            a = int(input("Digite um valor para o vetor : "))
            vetor.append(a)
        somaVetor(vetor)


Escolha()