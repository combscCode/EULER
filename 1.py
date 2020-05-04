
def getSumDivisibleBy(maxVal, divisor):
	p = maxVal // divisor
	return divisor*(p*(p+1))//2
target = 999
print(getSumDivisibleBy(target, 3) + getSumDivisibleBy(target, 5) - getSumDivisibleBy(target, 15))
