class Playfair:
    
    def createMatrix(self, key):
        import string

        letters = string.ascii_lowercase.replace('j', '.')
        key_matrix = [ '' for i in range(5) ]

        i = 0
        j = 0

        for c in key:
            if c in letters:
                key_matrix [i] += c

                letters = letters.replace(c, '.')
                
                j += 1
                if j > 4:
                    i += 1
                    j = 0

        for c in letters:
            if c != '.':
                key_matrix[i] += c

                j += 1
                if j > 4:
                    i += 1
                    j = 0


        return key_matrix

    def encrypt(self, message, key_matrix):
        messagePairs = []
        cryptogramPairs = []

        #Rule 1
        i = 0

        while i < len(message):

            a = message[i]
            b = ''

            if i + 1 == len(message):
                b = 'x'
            else:
                b = message[i+1]

            if a != b:
                messagePairs.append(a + b)
                i += 2
            else:
                messagePairs.append(a + 'x')
                i += 1
        #print(messagePairs)


        for pair in messagePairs:
            applied_rule = False

            #Rule 2
            for row in key_matrix:
                if pair[0] in row and pair[1] in row:
                    j0 = row.find(pair[0])
                    j1 = row.find(pair[1])

                    cryptogramPair = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                    cryptogramPairs.append(cryptogramPair)
                    applied_rule = True

            if applied_rule:
                continue

            #Rule 3
            for j in range(5):
                col = "".join([key_matrix[i][j] for i in range(5)])
                if pair[0] in col and pair[1] in col:
                    i0 = col.find(pair[0])
                    i1 = col.find(pair[1])

                    cryptogramPair = col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
                    cryptogramPairs.append(cryptogramPair)
                    applied_rule = True

            if applied_rule:
                continue

            #Rule 4
            i0 = 0
            i1 = 0
            j0 = 0
            j1 = 0
            for i in range(5):
                row = key_matrix[i]
                if pair[0] in row:
                    i0 = i
                    j0 = row.find(pair[0])

                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])

            cryptogramPair = key_matrix[i0][j1] + key_matrix[i1][j0]

            cryptogramPairs.append(cryptogramPair)
        result = "".join(cryptogramPairs)
        return result 


    def decrypt(self, cryptogram, key_matrix):
        messagePairs = []
        cryptogramPairs = []

        #Rule 1
        i = 0

        while i < len(cryptogram):

            a = cryptogram[i]
            b = cryptogram[i+1]

            cryptogramPairs.append(a + b)
            i += 2
        #print(cryptogramPairs)


        for pair in cryptogramPairs:
            applied_rule = False

            #Rule 2
            for row in key_matrix:
                if pair[0] in row and pair[1] in row:
                    j0 = row.find(pair[0])
                    j1 = row.find(pair[1])

                    messagePair = row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
                    messagePairs.append(messagePair)
                    applied_rule = True

            if applied_rule:
                continue

            #Rule 3
            for j in range(5):
                col = "".join([key_matrix[i][j] for i in range(5)])
                if pair[0] in col and pair[1] in col:
                    i0 = col.find(pair[0])
                    i1 = col.find(pair[1])

                    messagePair = col[(i0 + 4) % 5] + col[(i1 + 4) % 5]
                    messagePairs.append(messagePair)
                    applied_rule = True

            if applied_rule:
                continue

            #Rule 4
            i0 = 0
            i1 = 0
            j0 = 0
            j1 = 0
            for i in range(5):
                row = key_matrix[i]
                if pair[0] in row:
                    i0 = i
                    j0 = row.find(pair[0])

                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])

            messagePair = key_matrix[i0][j1] + key_matrix[i1][j0]

            messagePairs.append(messagePair)
        result = "".join(messagePairs)
        return result
            
        
    def breakPlayfair(self, cryptogram):
        with open("src\wordlist.txt", "r") as wordlist:
            for key in wordlist:
                key = key[:-1]
                key_matrix = self.createMatrix(key)
                message = self.decrypt(cryptogram, key_matrix)
                print(message)
        return cryptogram