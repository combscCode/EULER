'''
Find the first four consecutive integers that have four distinct primes each.

The first two ints that have 2 distinct are 
14 = 2x7
15 = 3x5

The first 3 to have 3 are
644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19
'''

from euler import distinct_primes_factors, generate_primes

def is_factorized_n_distinct_primes(n, x, primes):
	factors = distinct_primes_factors(x, primes)
	return len(factors) == n

def find_n_consecutive_ints(n, primes, start, stop):
	x = start
	while x < stop:
		#check
		if is_factorized_n_distinct_primes(n, x, primes):
			num = 1
			y = x
			while is_factorized_n_distinct_primes(n, y+1, primes):
				y += 1
				num += 1
			top = y
			if num < n:
				y -= n - 1
				while is_factorized_n_distinct_primes(n, y, primes) and y < x:
					y += 1
					num += 1
			x = top
			if num >= n:
				return top - n + 1
		x += n

if __name__ == '__main__':
	primes = generate_primes(n=4000)
	print('done generating primes')
	print(find_n_consecutive_ints(4,primes,2,1000000))
