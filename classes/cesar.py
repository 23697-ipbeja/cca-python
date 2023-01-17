letters = "abcdefghijklmnopqrstuvwxyz .,;:!?"

class Cesar:

    def __init__(self, message, key):
        self.message = message
        self.key = key

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