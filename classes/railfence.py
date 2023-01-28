class RailFence:

    def encrypt(self, message, key):

        cryptogram = ""
        cycle = key * 2 -2

        for row in range(key):
            index = 0

            # 1 Rail
            if row == 0:
                while index < len(message):
                    cryptogram += message[index]
                    index += cycle

            # last rail
            elif row == key -1:
                index = row
                while index < len(message):
                    cryptogram += message[index]
                    index += cycle

            # intermidiate rails
            else:
                left_index = row
                right_index = cycle - row
                while left_index < len(message):
                    cryptogram += message[left_index]

                    if right_index < len(message):
                        cryptogram += message[right_index]

                    left_index += cycle
                    right_index += cycle

        return cryptogram


    def decrypt(self, cryptogram, key):
        
        length = len(cryptogram)
        message = "." * length

        cycle = 2* key -2
        units = length // cycle

        rail_lenghts = [0] * key

        # Top Rail length
        rail_lenghts[0] = units

        # Intermediate Rail Lenght
        for i in range(1, key - 1):
            rail_lenghts[i] = 2 * units
        
        # Bottom Rail Lenght
        rail_lenghts[key-1] = units

        for i in range(length % cycle):
            if i < key:
                rail_lenghts[i] += 1
            else:
                rail_lenghts[cycle - i]
        
        # Replace chars in top rail
        index = 0
        rail_offset = 0
        for c in cryptogram[:rail_lenghts[0]]:
            message = message[:index] + c + message[index + 1:]
            index += cycle

        rail_offset += rail_lenghts[0]
        
        # Replace chars in intermediate rail
        for row in range(1, key -1):
            left_index = row
            right_index = cycle - row
            left_char = True
            for c in cryptogram[rail_offset:rail_offset + rail_lenghts[row]]:
                if left_char:
                    message = message[:left_index] + c + message[left_index + 1:]
                    left_index += cycle
                    left_char = not left_char
                else:
                    message = message[:right_index] + c + message[right_index + 1:]
                    right_index += cycle
                    left_char = not left_char
            rail_offset += rail_lenghts[row]

        # Replace chars in bottom rail
        index = key - 1
        for c in cryptogram[rail_offset:]:
            message = message[:index] + c + message[index + 1:]
            index += cycle

        rail_offset += rail_lenghts[0]

        return message

    def decryptFence(self, cipher, rails, offset=0):
        plain = ''

        # offset
        if offset:
            t = self.encrypt('o' * offset + 'x' * len(cipher), rails)
            for i in range(len(t)):
                if (t[i] == 'o'):
                    cipher = cipher[:i] + '#' + cipher[i:]

        length = len(cipher)
        fence = [['#'] * length for _ in range(rails)]

        # build fence
        i = 0
        for rail in range(rails):
            p = (rail != (rails - 1))
            x = rail
            while (x < length and i < length):
                fence[rail][x] = cipher[i]
                if p:
                    x += 2 * (rails - rail - 1)
                else:
                    x += 2 * rail
                if (rail != 0) and (rail != (rails - 1)):
                    p = not p
                i += 1

        # read fence
        for i in range(length):
            for rail in range(rails):
                if fence[rail][i] != '#':
                    plain += fence[rail][i]
        return plain