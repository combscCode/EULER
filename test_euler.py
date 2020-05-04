import euler
import math

def bitwise_length_test():
	assert (euler.bitwise_length(0) == 1)
	assert (euler.bitwise_length(1) == 1)
	assert (euler.bitwise_length(2) == 2)
	assert (euler.bitwise_length(3) == 2)
	assert (euler.bitwise_length(4) == 3)
	assert (euler.bitwise_length(5) == 3)
def sqrt_floor_test():
	for i in range(1000):
		assert( euler.sqrt_floor(i) == int(math.sqrt(i)))

if __name__ == '__main__':
	sqrt_floor_test()