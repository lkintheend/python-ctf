from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long, getStrongPrime
import sys

# from secret import flag

p = getStrongPrime(512)
q = getStrongPrime(512)
e = 65537

flag = 'matesctf{f1ll_d4t_b0ttl3!}'

byteFlag = bytes_to_long(flag)


class Server:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.e = e
        self.N = p * q
        phi = (p - 1) * (q - 1)
        self.d = inverse(self.e, phi)
        self.enc_flag = pow(byteFlag, self.e, self.N)

    def encrypt(self, message):
        if len(message) < 10:
            print
            "Your message is too short"
            sys.exit(1)
        m = bytes_to_long(message)
        if m >= self.N:
            print
            "Your message is too long"
            sys.exit(1)
        else:
            c = pow(m, self.e, self.N)
            c_flag = (pow(c, m, self.N) * self.enc_flag) % self.N
            return c, c_flag

    def decrypt(self, cipher):
        cipher = int(cipher)
        message = pow(cipher, self.d, self.N)
        return message


server = Server(p, q)
banner = "=" * 10 + "KoMA RSA service 4..0" + "=" * 10
menu = "1. Encrypt\n2. Decrypt\n3. Exit\n4. Publickey"

print
banner
while 1:
    try:
        print
        menu
        choice = int(raw_input("Your choice: ").strip())
        if choice == 1:
            message = raw_input("Your message: ").strip()
            cipher, cipher_flag = server.encrypt(message)
            print            "Your cipher: %d" % cipher
            print            "Your cipher_flag: %d" % cipher_flag
        elif choice == 2:
            cipher = raw_input("Your cipher: ").strip()
            message = server.decrypt(cipher)
            print            "Decrypted message: %d" % message
        elif choice == 3:
            print            "Thanks for using my service."
            sys.exit(1)
        elif choice == 4:
            print
            "Pubkey: {\"N\": %d, \"e\":%d}" % (server.N, server.e)
        else:
            print
            "Invalid choice"
    except:
        print
        "Bad input"
        sys.exit(1)
