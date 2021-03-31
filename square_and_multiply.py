def square_and_multiply(x, e, n):
    count = 0
    binary_e = bin(e) # First 2 character of string y is '0b', hence remove it. 
    binary_e = binary_e[2:]
    print ("Binary representation of e is : {}".format(binary_e))
    y = x
 
    for i in range(1, len(binary_e)):
      temp = y
      temp1 = (y * y) % n
      y = temp1
      count = count + 1

      if(binary_e[i] == '0'):
        print("0 => (Square) {}^2 mod {} = {}".format(temp, n, temp1))

      if(binary_e[i] == '1'):
        temp2 = (y * x) % n
        y = temp2
        count = count + 1

        print("1 => (Square and multiply) {}^2 mod {} = {} AND {}*{} mod {} = {}"\
          .format(temp, n, temp1, temp1, x, n, temp2))
        
    return y, count

print ("Format => y = x^e mod n")
x = int(input("x: "))
e = int(input("e: "))
n = int(input("n: "))
y, count = square_and_multiply(x, e, n)
print("y = {}".format(y))
print("total number of squares and Multiplication: {}".format(count))