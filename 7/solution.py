''' NOTES
adapted from 3
'''
import math

def find_mth_prime(m):
	primes = []
	i = 2
	num = 0
	while num < m:
		is_prime = True
		for prime in primes:
			if i % prime == 0:
				is_prime = False
				break
			if prime > math.sqrt( i ):
				break
		if is_prime:
			primes.append(i)
			num += 1
		i += 1
	print(primes)
	return primes[-1]

print(find_mth_prime(10001))
