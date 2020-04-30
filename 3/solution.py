''' NOTES

this question wants us to find the largest prime factor of some number

Strategy:
loop i from 1 to sqrt(n)

we need to build up our list of primes. If a number is not divisible by a prime then it is considered prime.

'''
import math
n = 600851475143 

def largest_prime_factor(m):
	largest = 1
	primes = []
	i = 2
	while i <= math.sqrt( m ):
		is_prime = True
		for prime in primes:
			if i % prime == 0:
				is_prime = False
				break
			if prime > math.sqrt( i ):
				break
		if is_prime:
			print(i)
			primes.append(i)
			if m % i == 0:
				largest = i
		i += 1
	print(primes)
	return largest

print(largest_prime_factor(n))
