#                                               
#   IPBEJA: ESTIG                               
#   MESI 22/23                                  
#   Criptografia e Criptoanalise Avan�adas     
#   Titulo: Exercicios Python                   
#   Autores: David Henriques (23697)            
#             Joao Tavanez (3109)               
# 
#                                              

from classes.cesar import Cesar
from classes.viginere import Viginere
from classes.affine import Affine
from classes.railfence import RailFence
from classes.playfair import Playfair
from classes.kasiski import Kasiski
import os
import time
import sys
import math
sys.getdefaultencoding()

# Clear Screen Windows/Linux
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

mainChoice = ""
subChoice = ""
cryptogram =""


# Menu
while mainChoice.lower() != "x":
    clearScreen()
    print("IPBEJA: ESTIG")
    print("MESI 22/23")
    print("Criptografia e Criptoanalise Avan�adas")
    print("Titulo: Exercicios Python")
    print("Autores: David Henriques (23697)")
    print("Joao Tavanez (3109)")
    print("")
    print("MENU DE TIPO DE CIFRA")
    print("")
    print("1: César")
    print("2: Viginere")
    print("3: Playfair")
    print("4: Rail-Fence")
    print("5: Affine")
    print("6: Metodo Kasiski")
    print("")
    print("Prima X Para Sair")
    print("")
    mainChoice = input("Por favor selecione uma opção ")
    
    match mainChoice.lower():
        
        # Cesar Cypher
        case "1":   

            while subChoice.lower() != "X":
                clearScreen()
                print("Cifra de Cesar")
                print("")
                print("Escolha a opção:")
                print("1: Cifrar")
                print("2: Decifrar")
                print("3: Quebrar a Cifra")
                print("")
                print("Prima X Para Sair")
                print("")
                subChoice = input("Por favor selecione uma opção ")
                print("")
                match subChoice.lower():
                    
                    case "1":
                        message = input("Insira a mensagem a cifrar: ")
                        print("")
                        while True:
                            user_input = input("Insira a chave (Valor Numerico): ")
                            if user_input.isnumeric():
                                key = int(user_input)
                                break
                            else:
                                print("")
                                print(user_input, "nao e um numero, tente novamente")
                                print("")
                        C = Cesar()
                        cryptogram = C.encrypt(message, key)
                        print("")
                        print("Criptograma: ", cryptogram)
                        
                        time.sleep(3)

                    case "2":
                        if cryptogram != "":
                            cryptogram = C.encrypt(message, key)
                            print("Cryptograma:", cryptogram)
                            print("")
                            plaintext = C.decrypt(cryptogram, key)
                            print("Mensagem:", plaintext)
                            time.sleep(3)

                        else:
                            print("É necessário cifrar primeiro")
                            time.sleep(2)
                    
                    case "3":
                        if cryptogram != "":
                            C.breakCesar(cryptogram)
                            print("Mesagem:", C.getMessage())
                            print("")
                            print("Chave:", C.getKey())
                            time.sleep(5)
                            
                        else:
                                print("É necessário cifrar primeiro")
                                time.sleep(2)
                    
                    case "x":
                        break
                    
                    case _:
                        print("Opção Inválida ")
                        time.sleep(2)             
        
        # Viginere Cypher        
        case "2":
            clearScreen()
            while subChoice.lower() != "X":
                print("")
                print("Cifra de Viginere")
                print("")
                print("Escolha a opção:")
                print("1: Cifrar")
                print("2: Decifrar")
                print("3: Quebrar a Cifra")
                print("")
                print("Prima X Para Sair")
                print("")
                subChoice = input("Por favor selecione uma opção ")
                print("")
                match subChoice.lower():
                    
                    case "1":
                        message = input("Insira a mensagem a cifrar: ")
                        print("")
                        while True:
                            user_input = input("Insira a chave (CHARS): ")
                            print("")
                            if user_input.isalpha():
                                key = str(user_input)
                                break
                            else:
                                print("")
                                print(user_input, "nao sao caracteres, tente novamente")
                                print("")
                        print("Message: ", message," Key: ", key)
                        print("")
                        V = Viginere()
                        cryptogram = V.encrypt(message, key)
                        print("Criptograma: ", cryptogram)
                        time.sleep(3)
                    
                    case "2":
                        if cryptogram != "":
                            print("")
                            plaintext = V.decrypt(cryptogram,key)
                            print("Mensagem: ", plaintext)
                            time.sleep(3)
                        else:
                            print("É necessário cifrar primeiro")
                            time.sleep(2)

                    
                    case "3":
                        cryptogram = "tenxm vmmaar nm ccgdt xba"
                        # criptograma cifrado com a chave "antonio que esta na wordlist"
                        print("Criptograma:  ", cryptogram)
                        print("")
                        V = Viginere()
                        plaintext = V.breakViginere(cryptogram)
                        print("Mensagem: ", plaintext)
                    
                    case "x":
                        clearScreen()
                        break
                    
                    case _:
                        print("Opção Inválida ")
                        time.sleep(2)         

        # Playfair Cypher
        case "3":
             clearScreen()
             while subChoice.lower() != "X":
                print("")
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
                        message = input("Insira a mensagem a cifrar: ")
                        print("")
                        while True:
                            user_input = input("Insira a chave (CHARS): ")
                            print("")
                            if user_input.isalpha():
                                key = str(user_input)
                                break
                            else:
                                print("")
                                print(user_input, "nao sao caracteres, tente novamente")
                                print("")
                        P = Playfair()
                        key_matrix = P.createMatrix(key)
                        cryptogram = P.encrypt(message, key_matrix)
                        print("Key: ", key)
                        print("Matrix: ", key_matrix)
                        print("Message: ", message)
                        print("Cryptogram: ", cryptogram)
                        print("")

                    case "2":
                        if cryptogram != "":
                            message = P.decrypt(cryptogram, key_matrix)
                            print("Cryptogram: ", cryptogram)
                            print("Message:", message)
                            time.sleep(3)
                            
                        else:
                            print("É necessário cifrar primeiro")
                            time.sleep(2) 

                    case "3":
                        cryptogram = "rmohwmqugwconafsepedlw"
                        # criptograma cifrado com a chave "portugal"
                        print("Criptograma: ", cryptogram)
                        print("")
                        P = Playfair()
                        print("Possiveis Mensagens: \n")
                        plaintext = P.breakPlayfair(cryptogram)
                        
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ") 
                        time.sleep(2)  

        # Rail-Fence Cypher          
        case "4":
             clearScreen()
             while subChoice.lower() != "X":
                print("")
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
                        message = input("Insira a mensagem a cifrar: ")
                        print("")
                        while True:
                            user_input = input("Insira a chave (Valor Numerico): ")
                            if user_input.isnumeric():
                                key = int(user_input)
                                break
                            else:
                                print("")
                                print(user_input, "nao e um numero, tente novamente")
                                print("")
                        R = RailFence()      
                        cryptogram = R.encrypt(message, key)
                        print("Cryptograma: ", cryptogram)
                        time.sleep(3)
                    
                    case "2":
                        if cryptogram != "":
                            print("")
                            plaintext = R.decrypt(cryptogram, key)
                            print("Mensagem: ", plaintext)
                            time.sleep(3)
                        
                        else:
                            print("É necessário cifrar primeiro")
                            time.sleep(3)
                    
                    case "3":
                        if cryptogram != "":
                            rails = range(2, 11)
                            offsets = range(0, 11)
                            for i in rails:
                                for j in offsets:
                                    print(R.decryptFence(cryptogram, i, offset=j))
                        
                        else:
                            print("É necessário cifrar primeiro")
                            time.sleep(3)
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ") 
                        time.sleep(2)  

        # Affine Cypher          
        case "5":
             clearScreen()
             while subChoice.lower() != "X":
                print("")
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
                        message = input("Insira a mensagem a cifrar: ")
                        print("")
                        print("Insira dois valores numericos para a chave")
                        print("")

                        while True:
                            user_input = input("Insira o primeiro numero: ")
                            if user_input.isnumeric() and math.gcd(int(user_input), 26) == 1:
                                a = int(user_input)
                                break

                            elif user_input.isnumeric() and math.gcd(int(user_input), 26) != 1:
                                print("")
                                print(user_input, "nao e um numero primo relativo com 26, tente novamente")
                                print("")                                
                            
                            else:
                                print("")
                                print(user_input, "nao e um numero, tente novamente")
                                print("")

                        while True:
                            user_input = input("Insira o segundo numero: ")
                            if user_input.isnumeric():
                                b = int(user_input)
                                break
                            else:
                                print("")
                                print(user_input, "nao e um numero, tente novamente")
                                print("")
                        A = Affine()                   
                        cryptogram = A.encrypt(message, a, b)
                        print("")
                        print("Criptograma: ", cryptogram)
                        time.sleep(3)
                        
                    case "2":
                        if cryptogram != "":
                            plaintext = A.decrypt(cryptogram, a, b)
                            print("Mensagem: ", plaintext)
                            time.sleep(3)

                        else:
                            print("É necessário cifrar primeiro")
                                        
                    case "3":
                        if cryptogram != "":
                            print("")
                            A.bruteForce(cryptogram)
                            time.sleep(3)

                        else:
                            print("É necessário cifrar primeiro")

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
                        Cryptogram = "atmebowemiwjfeaggrwvqqcwgmpgyeuhadmvusxgdeutariazcwfeuunqlwlqmxganwkeouwxhwjmlqeqnbgeeueqdqvmqcwacwfteigfeuhacwffulgzoakabmepeusuozydavvqzifatmeoouwanwlqmnayuuhamwwjtquaqcwzoxgpeawdrmhmrbapoxgpevvaevldebsztwhdodsdabgpoumzdwgzixjqsmffewlqmxgqsbwytcvaomigittdiwvmvqvmdmhqnlwqsawzcqsxmmffelwetmtqmambrmeaeymqmaggbmjoousoezlaaymmnbapalwpedssazggalwqsxwdaymqsmvqvmhdnikooqkmsvgoozjqncfoawjuskgmojmecijbozwxaavqdmxdovlmrawoougcumfapwjcumkmjckfauwpilspobwypwvmjckfavsfuzwlalsecwaeaa"
                        key_len = ""
                        key = ""
                        prob_messages = ""
                        K = Kasiski(key_len, key, prob_messages)
                        K.getMessage(Cryptogram)
                        print("A chave: ", K.getKey())
                        print("O Comprimento da chave: ", K.getKeyLenght())
                        time.sleep(5)
                        
                    
                    case "2":
                        Cryptogram = "atmebowemiwjfeaggrwvqqcwgmpgyeuhadmvusxgdeutariazcwfeuunqlwlqmxganwkeouwxhwjmlqeqnbgeeueqdqvmqcwacwfteigfeuhacwffulgzoakabmepeusuozydavvqzifatmeoouwanwlqmnayuuhamwwjtquaqcwzoxgpeawdrmhmrbapoxgpevvaevldebsztwhdodsdabgpoumzdwgzixjqsmffewlqmxgqsbwytcvaomigittdiwvmvqvmdmhqnlwqsawzcqsxmmffelwetmtqmambrmeaeymqmaggbmjoousoezlaaymmnbapalwpedssazggalwqsxwdaymqsmvqvmhdnikooqkmsvgoozjqncfoawjuskgmojmecijbozwxaavqdmxdovlmrawoougcumfapwjcumkmjckfauwpilspobwypwvmjckfavsfuzwlalsecwaeaa"
                        key_len = ""
                        key = ""
                        prob_messages = ""
                        K = Kasiski(key_len, key, prob_messages)
                        K.getMessage(Cryptogram)
                        print(K.decryptKasiski())
                        time.sleep(30)
                        
                    
                    case "x":
                        break
                    
                    case _:
                        print("Opcao Invalida ")
                        time.sleep(2)             

        case "x":
            print("Obrigado!")
            break
        case _:
            print("Opcao Invalida ")
            time.sleep(2)