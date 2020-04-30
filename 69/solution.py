
def generate_primes( n ):
	primes = [2]
	for i in range(3,n,2):
		is_prime = True
		for prime in primes:
			if i % prime == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(i)
	primes.insert(0, 1)
	return primes


