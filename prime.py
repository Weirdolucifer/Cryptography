import math

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
  
if __name__=='__main__': 
    n = 19682
    prime = SieveOfEratosthenes(n)
    x = int(math.sqrt(n))

    flag1 = 0
    flag2 = 0
    for i in range(x, n+1):
        if(prime[i] == True):
            if(flag1 != 1):
                flag1 = 1
            else:
                flag2 = 1 
            print(i)
        if( flag1 == 1 and flag2 == 1):
            break
