#                                               
#   IPBEJA: ESTIG                               
#   MESI 22/23                                  
#   Criptografia e Criptoanalise Avan�adas     
#   Titulo: Exercicios Python                   
#   Autores: David Henriques (23697)            
#             Jo�o Tavanez (3109)               
#                                               

#from classes.cesar import encrypt, decrypt, bruteForce
#from classes.viginere import encrypt, decrypt, bruteForce
#from classes.playfair import encrypt, decrypt, bruteForce
#from classes.rail_fence import encrypt, decrypt, bruteForce
#from classes.affine import encrypt, decrypt, bruteForce
import os

#Limpar Ecra Windows/Linux
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

mensagem = "Nos Somos do BENFICA - O Melhor!"
key = 9

#Menu
print("MENU DE TIPO DE CIFRA")
print("1: Cesar")
print("2: Viginere")
print("3: Playfair")
print("4: Rail-Fence")
print("5: Affine")
print("6: Metodo Kasiski")
print("")
print("Prima X Para Sair")
choice = input("Por favor selecione uma opcao ")

match choice:
    case "1":
        clearScreen()
        print("Cifra de Cesar")
        print("Mensagem:", mensagem)
        print("Chave", key)

        print("Escolha a opcao:")
        print("1: Cifrar")
        print("2: Decifrar")
        print("3: Quebrar a Cifra")
        opcao = input("Por favor selecione uma opcao ")

        match opcao:
            case "1":
                cesar.cifrar()
            case "2":
                cesar.decifrar()
            case "3":
                cesar.bruto()
            case _:
                print("Opcao Invalida ")             
            
    case "2":
        print("Viginere")

    case "3":
        print("Playfair")

    case "4":
        print("Rail-Fence")

    case "5":
        print("Affine")
    
    case "6":
        kasisky.comprimento()
        kasisky.decifrar()
    
    case "x":
        print("Adeus")
    case _:
        print("Opcao Invalida ")