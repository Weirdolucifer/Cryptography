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

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)

def main():
	a = int(input("Input first integer: "))
	b = int(input("Input second integer: "))
	print("GCD of numbers: ",gcd(a,b))
	x, y = extendedEuclid(a, b)
	print("coefficient of A:", x)
	print("coefficient of B:", y)
	print("Extended Euclid Equaton:",a,"*",x,"+",b,"*",y,"=",gcd(a,b))
	print("Modular Multiplicative Inverse of {} is {}".format(a,x%b))


if __name__ == "__main__":
    main();