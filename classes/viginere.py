letters = "abcdefghijklmnopqrstuvwxyz .,;:?!-"

class Viginere:

    def __init__(self, message, key):
        self.message = message
        self.key = key

    def encrypt(self, message, key):
        result = ""
        for i in range(len(message)):
            if message[i] in letters:
                cur_key = letters.index(key[i%len(key)])
                result += letters[(letters.index(message[i]) + cur_key) % len(letters)]
            else:
                result += message[i]
        return result

    def decrypt(self, cryptogram, key):
        result = ""
        for i in range(len(cryptogram)):
            if cryptogram[i] in letters:
                cur_key = letters.index(key[i%len(key)])
                result += letters[(letters.index(cryptogram[i]) - cur_key) % len(letters)]
            else:
                result += cryptogram[i]
        return result

