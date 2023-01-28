from collections import Counter
import math, re

chars = "abcdefghijklmnopqrstuvwxyz"
FREQ={  'a':13.9, 'b':1.0, 'c':4.4, 'd':5.4, 'e':12.2, 'f':1.0,
    'g':1.2, 'h':0.8, 'i':6.9, 'j':0.4, 'k':0.1, 'l':2.8,
    'm':4.2, 'n':5.3, 'o':10.8, 'p':2.9, 'q':0.9, 'r':6.9,
    's':7.9, 't':4.9, 'u':4.0, 'v':1.3, 'w':0.0, 'x':0.3,
    'y':0.0, 'z':0.4, ' ':0, '.':0, ',':0
}

key=""
minimum=5
maximum=8

class Kasiski:

    def __init__(self, key_len, key, prob_messages):
        self.key_len = key_len
        self.key = key
        self.prob_messages = prob_messages
         

    def decrypt(self, cryptogram, key):
            message=""
            for i in range(len(cryptogram)):
                    val_i = chars.find(cryptogram[i].lower())
                    val_k = chars.find(key[i%len(key)])
                    msg = chars[(val_i-val_k)%len(chars)]
                    message += msg
            return message

    def difference(self, text):
            counter = Counter(text)
            total = 0
            for letter in chars:
                    cur_difference = (counter[letter] * 100) / len(text) - FREQ[letter]
                    total += abs(cur_difference)
            total = total / len(chars)
            return total

    def brk(self, cryptogram):
            lowest_difference = math.inf
            for cur_key in chars:
                    current_message = self.decrypt(cryptogram, cur_key)
                    current_difference = self.difference(current_message)
                    if current_difference < lowest_difference:
                            lowest_difference = current_difference
                            key = cur_key
            return (key, self.decrypt(cryptogram, key))

    def find_reps(self, txt):
        result = {}
        for i in range(len(txt)):
            for j in range(minimum, maximum):
                if i+j > len(txt): break
                cur = txt[i:i+j]
                if cur not in result: result[cur] = 0
                result[cur] += 1
        return result

    def getMessage(self, C):
        reps=self.find_reps(C)
        # obter as strings que mais se repetem
        c=[]
        v=0
        for r in reps:
            if reps[r] > v:
                v=reps[r]
                c=[r]
                
            elif reps[r] == v:
                c.append(r)
        
        # calcular as distancias entre as repeticoes e respetivos divisores
        diffs = {}
        for a in c:
            found = [m.start() for m in re.finditer(a, C)]
            for i in range(len(found)-1):
                d = found[i+1]-found[i]
                for j in range(minimum,d):
                    if d % j == 0:
                        if j not in diffs: diffs[j] = 0
                        diffs[j] += 1

        # obter os divisores mais comuns
        c=[]
        v=0
        for i in diffs:
            if i > maximum: continue
            if diffs[i] > v:
                c = [i]
                v=diffs[i]
            elif diffs[i] == v:
                c.append(i)

        #temos as possiveis dimensoes de chaves
        #bruteforce com as dimensoes das chaves
        keys=[]
        for key_len in c:
            key = ""
            # temos uma dimensao da chave, percorremos caractere a caracter
            # cifrando pedaços de texto das respetivas posicoes
            for x in range(key_len):
                msg = ""
                for i in range(x, len(C), key_len):
                    msg += C[i]
                key += self.brk(msg)[0]
            keys.append(key)
        
        #print(keys)
        prob_messages = []
        lowest_difference = math.inf

        # decifrar com todas as chaves e testar qual a melhor

        for key in keys:
            cur_message = self.decrypt(C, key)
            diff = self.difference(cur_message)
            if diff < lowest_difference:
                lowest_difference = diff
                prob_messages = [[cur_message]]
            elif diff == lowest_difference:
                prob_messages.append([cur_message])
            self.key = key.upper()
            self.prob_messages = prob_messages

    def getKey(self):
        x = int(len(self.key) / 2)
        self.key = [self.key[i:i+x] for i in range(0, len(self.key), x)]
        if self.key[0] == self.key[1]:
            self.key = self.key[0]
        return self.key

    def getKeyLenght(self):
        self.key_len = len(self.key)
        return self.key_len

    def decryptKasiski(self):
        return self.prob_messages

    


