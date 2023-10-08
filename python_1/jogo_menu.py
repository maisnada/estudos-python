import jogo_forca
import jogo_adivinha

def escolhe_jogo():

    print("**********************************")
    print("Bem vindo escolha seu jogo")
    print("**********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    print("\n")

    if(jogo == 1):
        jogo_forca.jogar()
        
    elif(jogo ==2):
        jogo_adivinha.jogar()
 
#ao executar o script direto o pyhton define a variável __name__, já via import não    
if(__name__ == "__main__"):
    escolhe_jogo()
   