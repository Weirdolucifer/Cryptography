import sys

encrypted_message_in_blocks = []

# y = x^e % n
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


# Part 2: Encryption:
def encrypt(message, public_key, block_size):
    n, e = public_key
    i = 0
    while(i < len(message)):
        computed_message = 0
        for j in range(block_size):
            if(message[i].isupper()):
                temp = ord(message[i])-65
            else:
                temp = 26

            computed_message = computed_message + temp*(27**(block_size-1-j))

            i = i + 1
            if( i == len(message)):
                while(j < block_size-1):
                    temp = 26
                    j = j + 1
                    computed_message = computed_message + temp*(27**(block_size-1-j))
                break

        encrypted_message = square_and_multiply(computed_message, e, n)
        encrypted_message_in_blocks.append(encrypted_message)

    return encrypted_message_in_blocks

def main(public_key, block_size):
    message = input("Enter message: ")
    print('Encrypting the message...')
    encrypted_message_in_blocks = encrypt(message, public_key, block_size)
    print("Encrypted Message: {}".format(encrypted_message_in_blocks))

if __name__=='__main__':

    # 1st argv: public key (n)
    # 2nd argv: public key (e)
    # 3rd argv: block size of message  
    main((int(sys.argv[1]), int(sys.argv[2])), int(sys.argv[3]))

