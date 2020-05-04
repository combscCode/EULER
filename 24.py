'''
NOTES
We can think of these permutations being laid out into sections

for a permutation of n elements:
let m be the number of permutations available

there are n sections of size (m/n) that make up the total list of perms
which of these sections you land in determines the first number in the permutation.

Let C be the cth permutation that we're looking for

the first element of C will be c//(m/n)
c can range from 0 to m, so c//(m/n) ranges from 0 to n

we then mod c by c % (m/n)
if it's in the first section it doesn't change, but if it's in the last section it should change a lot.


the second element of C will now be c//(m/n-1)
c can range from 0 to m, so c//(m/n-1) ranges from 0 to n-1


and so on and so on.

'''
import math

def find_perm(c, vals):
	#c should be the cth permutation
	n = len(vals)
	m = math.factorial(n)
	permutation = ''
	while n > 0:
		idx = int(c // (m/n))
		permutation += vals[idx]
		vals.pop(idx)
		c %= (m/n)
		m /= n
		n -= 1
	return permutation
vals = ['0','1','2','3','4','5','6','7','8','9']
print( find_perm(1e6 - 1, vals) )
