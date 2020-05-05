''' NOTES

this question wants us to find the largest prime factor of some number

Strategy:
loop i from 1 to sqrt(n)

we need to build up our list of primes. If a number is not divisible by a prime then it is considered prime.

'''
from euler import generate_primes, sqrt_floor
import math
n = 600851475143 
test = 123123123

def previous_solution(m):
	largest = 1
	primes = []
	i = 2
	while i <= math.sqrt( m ):
		is_prime = True
		for prime in primes:
			if i % prime == 0:
				is_prime = False
				break
			if prime > sqrt_floor( i ):
				break
		if is_prime:
			primes.append(i)
			if m % i == 0:
				largest = i
		i += 1
	return largest

def new_solution(m):
	largest = 1
	primes = generate_primes(greatest=sqrt_floor(m))
	for p in primes:
		if m % p == 0:
			largest = p
	return largest
print(new_solution(n))