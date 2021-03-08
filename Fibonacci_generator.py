'''
Takes the code for obtaining a Fibonacci sequence starting at a given offset
with a recursive function but uses a generator function instead for better efficiency.
'''


def fibonacci(rng, offset = 0):
    '''
	This function generates a Fibonnaci sequence by calling on another generator function,
	but only returns the values after a given offset.
	'''
    count = 0
    n = offset + rng
    for i in fib_gen(n):
        count += 1
        if count < offset: pass
        else: yield i

def fib_gen(n):
	''' Generator function that returns the Fibonacci sequence '''
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b

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
