'''
NOTES


even denom can't have even numerator

'''
import math

max_d = 12000
primes = [2]
for i in range( 3, int(math.sqrt(max_d+1)) ):
	is_prime = True
	for p in primes:
		if i % p == 0:
			is_prime = False
			break
	if is_prime:
		primes.append(i)

def is_reduced(n, d):
	if n == 0:
		return d == 1
	return is_reduced( d%n, n )


# counts the # of reduced fractions for denom d between (x, y) exclusive
def count_reduced_fractions( x, y, d ):
	reduced = 0
	d_is_even = d%2==0
	
	start = int(x * d + 1)
	if d_is_even and start%2 == 0:
		start += 1
	end = math.ceil(y * d)
	
	r = range( start, end, 2 ) if d_is_even else range( start, end )
	
	for i in r:
		if is_reduced(i, d):
			reduced += 1
	return reduced

s = 0
for z in range(1,12001):
	s += count_reduced_fractions( 1/3, 1/2, z )
print(s)
