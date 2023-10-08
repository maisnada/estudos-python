import random

def jogar():

    print("\033[1;35;40m**********************************")
    print("Bem vindo no jogo de adivinhação")
    print("**********************************")

    #número de 1 a 100
    numero = random.randrange(1,101)

    total_de_tentativas = 0

    rodada = 1

    pontos = 1000

    print("\033[1;33;40mQual o nível de dificuldade? [{}]".format(numero))
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Informe o nível: "))

    if(nivel ==1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        
        print("\n\033[1;34;40m>>Tentativa {} de {}".format(rodada , total_de_tentativas))
        
        digitado = int (input("Infome um número de 1 a 100: "))
        
        if(digitado < 1 or digitado > 100):
            print("\033[1;31;40mValor deve ser entre 0 e 100!")
            continue     

        acertou = digitado == numero
        maior   = digitado > numero
        menor   = digitado < numero

        if(acertou):
            print("\n\033[1;32;40mVocê acertou e fez {} pontos! ;D".format(pontos))
            break
        else:    
            if(maior):
                print("\033[1;31;40mVocê errou ;[ .. O valor é maior que número oculto")
            elif(menor):
                print("\033[1;31;40mVocê errou ;[ .. O valor é menor que número oculto")    

            #modulo da operação/número absoluto
            pontos_perdidos = abs(numero - digitado)
            
            pontos = pontos - pontos_perdidos
            
        rodada += 1 
        
    print("\n\033[1;37;40mFim do jogo...")


#ao executar o script direto o pyhton define a variável __name__, já via import não    
if(__name__ == "__main__"):
    jogar()


