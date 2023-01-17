#                                               
#   IPBEJA: ESTIG                               
#   MESI 22/23                                  
#   Criptografia e Criptoanalise Avan�adas     
#   Titulo: Exercicios Python                   
#   Autores: David Henriques (23697)            
#             Jo�o Tavanez (3109)               
#                                               

from classes.cesar import Cesar
import os
import time

# Clear Screen Windows/Linux
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

message = "herois do mar nobre povo"
key = 35
mainChoice = ""
subChoice = ""


# Menu
while mainChoice.lower() != "x":
    clearScreen()
    print("MENU DE TIPO DE CIFRA")
    print("")
    print("1: Cesar")
    print("2: Viginere")
    print("3: Playfair")
    print("4: Rail-Fence")
    print("5: Affine")
    print("6: Metodo Kasiski")
    print("")
    print("Prima X Para Sair")
    print("")
    mainChoice = input("Por favor selecione uma opcao ")
    
    match mainChoice.lower():
        
        # Cesar Cypher
        case "1":   

            while subChoice.lower() != "X":
                clearScreen()
                print("Cifra de Cesar")
                print("")
                print("Escolha a opcao:")
                print("1: Cifrar")
                print("2: Decifrar")
                print("3: Quebrar a Cifra")
                print("")
                print("Prima X Para Sair")
                print("")
                subChoice = input("Por favor selecione uma opcao ")
                print("")
                match subChoice.lower():
                    
                    case "1":
                        msgKeyCesar = Cesar(message,key)
                        encrypt = msgKeyCesar.encrypt(message,key)
                        print(encrypt)
                        time.sleep(3)

                    case "2":
                        msgKeyCesar = Cesar(message,key)
                        cryptogram = msgKeyCesar.encrypt(message,key)
                        print(cryptogram)
                        print("")
                        decrypt = msgKeyCesar.decrypt(cryptogram,key)
                        print(decrypt)
                        time.sleep(3)
                    
                    case "3":
                        print("cesar.bruto()")
                    
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ")
                        time.sleep(2)             
        
        # Viginere Cypher        
        case "2":

            while subChoice.lower() != "X":
                            clearScreen()
                            print("Cifra de Viginere")
                            print("")
                            print("Escolha a opcao:")
                            print("1: Cifrar")
                            print("2: Decifrar")
                            print("3: Quebrar a Cifra")
                            print("")
                            print("Prima X Para Sair")
                            print("")
                            subChoice = input("Por favor selecione uma opcao ")
                            print("")
                            match subChoice.lower():
                                
                                case "1":
                                    print("viginere.cifrar()")
                                
                                case "2":
                                    print("viginere.decifrar()")
                                
                                case "3":
                                    print("viginere.bruto()")
                                
                                case "x":
                                    break
                                
                                case _:
                                    print("Opcao Invalida ")
                                    time.sleep(2)         

        # Playfair Cypher
        case "3":

             while subChoice.lower() != "X":
                clearScreen()
                print("Cifra de Playfair")
                print("")
                print("Escolha a opcao:")
                print("1: Cifrar")
                print("2: Decifrar")
                print("3: Quebrar a Cifra")
                print("")
                print("Prima X Para Sair")
                print("")
                subChoice = input("Por favor selecione uma opcao ")
                print("")
                match subChoice.lower():
                    
                    case "1":
                        print("Playfair.cifrar()")
                    
                    case "2":
                        print("Playfair.decifrar()")
                    
                    case "3":
                        print("Playfair.bruto()")
                    
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ") 
                        time.sleep(2)  

        # Rail-Fence Cypher          
        case "4":
             while subChoice.lower() != "X":
                clearScreen()
                print("Cifra de Rail-Fence")
                print("")
                print("Escolha a opcao:")
                print("1: Cifrar")
                print("2: Decifrar")
                print("3: Quebrar a Cifra")
                print("")
                print("Prima X Para Sair")
                print("")
                subChoice = input("Por favor selecione uma opcao ")
                print("")
                match subChoice.lower():
                    
                    case "1":
                        print("RailFence.cifrar()")
                    
                    case "2":
                        print("RailFence.decifrar()")
                    
                    case "3":
                        print("RailFence.bruto()")
                    
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ") 
                        time.sleep(2)  

        # Affine Cypher          
        case "5":
             while subChoice.lower() != "X":
                clearScreen()
                print("Cifra de Affine")
                print("")
                print("Escolha a opcao:")
                print("1: Cifrar")
                print("2: Decifrar")
                print("3: Quebrar a Cifra")
                print("")
                print("Prima X Para Sair")
                print("")
                subChoice = input("Por favor selecione uma opcao ")
                print("")
                match subChoice.lower():
                    
                    case "1":
                        print("Affine.cifrar()")
                    
                    case "2":
                        print("Affine.decifrar()")
                    
                    case "3":
                        print("Affine.bruto()")
                    
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ") 
                        time.sleep(2)     

        # Kasiski Method on Viginere Cypher      
        case "6":
             while subChoice.lower() != "X":
                clearScreen()
                print("Kasiski Method")
                print("")
                print("Escolha a opcao:")
                print("1: Comprimento")
                print("2: Decifrar")
                print("")
                print("Prima X Para Sair")
                print("")
                subChoice = input("Por favor selecione uma opcao ")
                print("")
                match subChoice.lower():
                    
                    case "1":
                        print("comprimento")
                    
                    case "2":
                        print("decifrar")
                    
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ")
                        time.sleep(2)             

        case "x":
            print("Adeus")
            break
        case _:
            print("Opcao Invalida ")