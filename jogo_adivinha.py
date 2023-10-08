print("teste ação.")
print("**********************************")
print("Bem vindo no jogo de adivinhação")
print("**********************************")

numero = 36

total_de_tentativas = 3

rodada = 1

while(rodada <= total_de_tentativas):
    
    print("\n>>Tentativa {} de {}".format(rodada, total_de_tentativas))
    
    digitado = int (input("Infome um número: "))
    
    print("Valor informado foi:", digitado)

    acertou = digitado == numero
    maior   = digitado > numero
    menor   = digitado < numero

    if(acertou):
        print("Você acertou! ;D")
    else:    
        if(maior):
            print("Você errou ;[ .. O valor é maior que número oculto")
        elif(menor):
            print("Você errou ;[ .. O valor é menor que número oculto")    
    
    rodada += 1 
    
print("Fim do jogo...")

