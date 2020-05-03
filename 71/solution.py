'''
NOTES

for some fraction n/d, if n/d < 1 and HCF(n,d)=1 it's reduced proper fraction.
So if it just can't be reduced anymore and less than 1.

ok we're looking for the fraction that is the closest to 3/7 while still being less and we can choose any n,d st n/d <= 1000000


'''

target = 3/7
d = int(1e6)
best_n = 0
best_d = 1
best_approx = 0

for new_d in range( 2, d + 1 ):
	new_n = int( new_d * target )
	current = new_n / new_d
	if current > best_approx and current != target:
		best_approx = current
		best_n = new_n
		best_d = new_d

print( best_n )
print( best_d )
