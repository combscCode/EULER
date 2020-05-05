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

def gcf_test():
	assert (euler.gcf(1,1) == 1)
	assert (euler.gcf(1,2) == 1)
	assert (euler.gcf(2,3) == 1)
	assert (euler.gcf(8,4) == 4)
	assert (euler.gcf(50,175) == 25)
	assert (euler.gcf(7,13) == 1)

if __name__ == '__main__':
	bitwise_length_test()
	sqrt_floor_test()
	gcf_test()