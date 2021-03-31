import math
import sender

# base functions needed 
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def extendedEuclid(a, b):
    if b == 0:
        x = 1
        y = 0
    else:
        x, y = extendedEuclid(b, a%b)
        temp = x
        x = y
        y = temp - (a//b)*y
    return x, y

def square_and_multiply(x, e, n):
    binary_e = bin(e) # First 2 character of string y is '0b', hence remove it. 
    binary_e = binary_e[2:]
    y = x
 
    for i in range(1, len(binary_e)):
      temp = y
      temp1 = (y * y) % n
      y = temp1

      if(binary_e[i] == '1'):
        temp2 = (y * x) % n
        y = temp2
        
    return y

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 

        if (prime[p] == True): 

            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False

    return prime

# Part 1: Key generation
def key_generation(block_size):
    key = 27
    key_space = (key**block_size) - 1

    # Step 1: selecting prime numbers:
    prime = SieveOfEratosthenes(key_space)
    x = int(math.sqrt(key_space))

    p = 0
    q = 0
    for i in range(x, key_space+1):
        if(prime[i] == True):
            if(p == 0):
                p = i
            else:
                q = i

        if(p != 0 and q != 0):
            break

    print("p: {}".format(p))
    print("q: {}".format(q))

    n = p*q

    # Step 2: computing phi
    phi = (p-1)*(q-1)

    # Step 3: Choosing e
    e = 1
    for i in range(2, phi-1):
        if(gcd(i,phi) == 1):
            e = i
            break

    # Step 4: Computing d
    x, y = extendedEuclid(e, phi)
    d =  x % phi

    # Step 5: public key and private key
    public_key = (n, e)
    private_key = (n, d)

    print("Public Key: {}".format(public_key))
    print("Private Key: {}".format(private_key))

    return public_key, private_key

# Part 3: Decryption:
def decrypt(encrypted_message_in_blocks, private_key, block_size):
    n, d = private_key
    message = ""
    for encrypted_message in encrypted_message_in_blocks:
        decrypted_message = square_and_multiply(encrypted_message, d, n)
        block_message = ""
        for j in range(block_size):
            temp = decrypted_message % 27
            if(temp != 26):
                block_message = block_message + chr(temp+65)
            else:
                block_message = block_message + " "

            decrypted_message= decrypted_message - temp
            decrypted_message = decrypted_message // 27

        message = message + block_message[:: -1]
    return message

if __name__=='__main__': 
	
    block_size = int(input("Enter the block size: "))
    
    print('Generating the keys...')
    public_key, private_key = key_generation(block_size)

    print('Sending Public Key and Block size to sender...')
    sender.main(public_key, block_size)

    print('Decrypting the message using private key...')
    decrypted_message = decrypt(sender.encrypted_message_in_blocks, private_key, block_size)
    print("Decrypted Message: {}".format(decrypted_message))

