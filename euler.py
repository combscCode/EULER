# This file contains functions that are helpful for solving math problems.
# My goal was to do everything from scratch
import warnings
import math

def bitwise_length(x):
	if x == 0:
		return 1
	if not isinstance( x, int ):
		warnings.warn('bitwise_length parameter must be an int')
		raise RuntimeError
	length = 0
	while x != 0:
		x >>= 1
		length += 1
	return length

def log2_floor(x):
	return bitwise_length(int(x))

def sqrt_approx(x, delta):
	if x < 0:
		warnings.warn('sqrt_approx parameter must be >= 0')
		raise RuntimeError
	estimate = 1 << ( log2_floor( x ) // 2 )
	change = delta + 1
	while change > delta:
		new_estimate = 0.5 * (estimate + x/estimate)
		change = abs(new_estimate - estimate)
		estimate = new_estimate
	return estimate

# Babylonian Method
def sqrt_floor( x ):
	if x < 0:
		warnings.warn('sqrt_floor parameter must be >= 0')
		raise RuntimeError
	estimate = int(sqrt_approx(x, 0.05))
	if (estimate - 1)**2 == x:
		return estimate - 1
	return estimate

def generate_primes(n=None, greatest=None, include_one=False):
	if n is None and greatest is None or n is not None and greatest is not None:
		warnings.warn('when generating primes specify either the amount you want generated or the maximum number allowed')
		raise RuntimeError
	primes = []
	if n is not None:
		if include_one:
			n -= 1
	m = 0
	i = 2
	if n is not None:
		while m < n:
			is_prime = True
			for p in primes:
				if i % p == 0:
					is_prime = False
					break
				if p > sqrt_floor( i ):
					break
			if is_prime:
				primes.append(i)
				m += 1
			i += 1
	if greatest is not None:
		while i < greatest:
			is_prime = True
			for p in primes:
				if i % p == 0:
					is_prime = False
					break
				if p > sqrt_floor( i ):
					break
			if is_prime:
				primes.append(i)
			i += 1
	if include_one:
		primes.insert(0, 1)
	return primes

#implemented using euclidean method
def gcf(a, b):
	while b:
		a, b = b, a%b
	return a

def is_reduced_fraction(n,d):
	return gcf(n,d) == 1

def factor_int(n,primes):
	if n == 0:
		warnings.warn('factor_int: factoring 0 doesnt make sense')
		raise RuntimeError
	factors = []
	for p in primes:
		while n % p == 0:
			factors.append(p)
			n /= p
	return factors

def distinct_primes_factors(n,primes):
	return set(factor_int(n,primes))

def ceil(a, b):
	return a//b+(a%b!=0)

def ceil(n):
	return n + (n - int(n) != 0)

if __name__ == '__main__':
	print("Feel free to take a look through the project to see my solutions!")