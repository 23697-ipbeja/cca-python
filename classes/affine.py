class Affine:

    import math

    def encrypt(self, plaintext, a, b):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                x = (a * (ord(char.upper()) - ord('A')) + b) % 26
                ciphertext += chr(x + ord('A'))
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext, a, b):
        # modular inverse of a
        a_inv = 0
        for i in range(0, 26):
            if (a*i)%26 == 1:
                a_inv = i
                break
        # decrypt the ciphertext
        plaintext = ""
        for c in ciphertext:
            if c.isalpha():
                x = ord(c) - ord('A')
                y = (a_inv*(x-b)) % 26
                plaintext += chr(y + ord('A'))
        return plaintext

    def bruteForce(self, ciphertext):
        for a in range(1, 26):
            for b in range(0, 26):
                if self.math.gcd(a, 26) == 1:
                    plaintext = self.decrypt(ciphertext, a, b)                    
                    print(f"a: {a:>2} b: {b:>2}  {plaintext:>10}")
                


