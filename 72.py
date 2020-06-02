from euler import is_reduced_fraction, ceil

# counts the # of reduced fractions for denom d between (x, y) exclusive
def count_reduced_fractions( x, y, d ):
	reduced = 0
	d_is_even = d%2==0
	
	start = int(x * d + 1)
	if d_is_even and start%2 == 0:
		start += 1
	end = ceil(y * d)
	
	r = range( start, end, 2 ) if d_is_even else range( start, end )
	
	for i in r:
		if is_reduced_fraction(i, d):
			reduced += 1
	return reduced

d = int(1e4)
#d = int(8)
print(d)

s = 0
for z in range(1,d+1):
	s += count_reduced_fractions( 0, 1, z )
print(s)
