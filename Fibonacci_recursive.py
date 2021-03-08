'''
Script for obtaining a Fibonacci sequence that starts at a given offset,
using a recursive function.
'''

def fibonacci(rng, offset = 0):
	'''
	This function generates a Fibonnaci sequence by calling on another function
	to obtain the first two numbers after a given offset. For efficiency reasons,
	the following numbers in the sequence range are obtained by iterative addition.
	'''
	a = offset
	b = offset + rng
	count = 0
	for i in range(a,b):
		count += 1
		if count == 1:
			first = fib_rec(i)
			yield first
		elif count == 2:
			second = fib_rec(i)
			yield second
		else:
			next_pos = first + second
			yield next_pos
			first = second
			second = next_pos

def fib_rec(n):
	'''
	Recursive function that returns the Fibonacci number for a given position in the sequence.
	'''
	if n == 0: return 0
	elif n == 1: return 1
	else: return fib_rec(n-1) + fib_rec(n-2)


def inpt():
	'''
	Function devised to handle exceptions in the input of the parameters for fibonacci()
	'''
	def rng():
		while True:
			try:
				r = int(input("Introduce desired number of Fibonacci sequence values:\n"))
				break
			except:
				print("Introduce an integer")
				pass
		return r

	def offset():
		try: o = int(input("Introduce first number in sequence offset:\n"))
		except:
			print("Using default offset")
			o = 0
		finally: return o

	return rng(), offset()


def main():
	rng, offset = inpt()
	for f in fibonacci(rng, offset): print(f)

if __name__ == '__main__':
	main()
