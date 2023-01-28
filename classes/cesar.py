letters = "abcdefghijklmnopqrstuvwxyz .,;:!?"
import math
from collections import Counter
LETTER_FREQUENCY = {"a":13.9, "b":1.0, "c":4.4, "d":5.4, "e":12.2, "f":1.0, "g":1.2, "h":0.8, "i":6.9, "j":0.4, "k":0.1, "l":2.8, "m":4.2,
 "n":5.3, "o":10.8, "p":2.9, "q":0.9, "r":6.9, "s":7.9, "t":4.9, "u":4.0, "v":1.3, "w":0.0, "x":0.3, "y":0.0, "z":0.4, " ":0.0, ".":0.0, ",":0.0, ";":0.0, ":":0.0, "!":0.0,"?":0.0}

class Cesar:

    def __init__(self, message = None, key = None):
        self.__message = message
        self.__key = key
        if message != None and key != None:
            self.__cryptogram = self.encrypt(message, key)
        else:
            self.__cryptogram = None

    def encrypt(self, message, key):
        result= ""
        for i in message.lower():
            if i in letters:
                cur_letter = letters[(letters.index(i) + key) % len(letters)]
                result += cur_letter
            else:
                result += i
        return result

    def decrypt(self, cryptogram, key):
        result = ""
        for i in cryptogram.lower():
            if i in letters:
                cur_letter = letters[(letters.index(i) - key) % len(letters)]
                result += cur_letter
            else:
                result += i
        return result

    def difference(self, text):
        c = Counter(text)
        total = 0
        for letter in letters:
            current_difference = c[letter] * 100 / len(text) - LETTER_FREQUENCY[letter]
            total += abs(current_difference)
        return total / len(letters)

    def breakCesar(self, cryptogram):
        lowest_difference = math.inf
        key = 0
        message = None
        for cur_key in range(len(letters)):
            cur_message = self.decrypt(cryptogram, cur_key)
            current_difference = self.difference(cur_message)
            #print(cur_key, current_difference)
            if current_difference < lowest_difference:
                    lowest_difference = current_difference
                    key = cur_key
                    message = cur_message

        self.__message = message
        self.__key = key
        self.__cryptogram = cryptogram
        return message

    def getMessage(self):
        return self.__message

    def getCryptogram(self):
        return self.__cryptogram
    
    def getKey(self):
        return self.__key