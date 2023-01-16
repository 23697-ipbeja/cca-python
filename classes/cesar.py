class Cesar:

    def __init__(self, message = None, key = None):
        self.__message = message
        self.__key = key
        if message != None and key != None:
            self.__cryptogram = self.encrypt(message, key)
        else:
            self.__cryptogram = None

    def encrypt(self, message, key):
        self.__message = message
        self.__key = key
        result= ""
        for i in range(len(message)):
            cur_char = message[i].lower()
            if message[i] in letters:
                cur_letter = letters[(letters.index(message[i]) + key) % len(letters)]
                if message[i].isupper():
                    result += cur_letter.upper()
                else:
                    result += cur_letter
            else:
                result += message[i]
        self.__cryptogram = result
        return result

    def decrypt(self, cryptogram, key):
        self.__cryptogram = cryptogram
        self.__key = key
        result = ""
        for i in range(len(cryptogram)):
            cur_char = cryptogram[i].lower()
            if cryptogram[i] in letters:
                cur_letter = letters[(letters.index(cryptogram[i]) - key) % len(letters)]
                if cryptogram[i].isupper():
                    result += cur_letter.upper()
                else:
                    result += cur_letter
            else:
                result += cryptogram[i]
        self.__message = result
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
            print(cur_key, current_difference)
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