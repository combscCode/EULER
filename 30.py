
total = []
for i in range(2, 200000):
	digit_sum = 0
	curr = i
	while curr > 0:
		digit_sum += (curr % 10)**5
		curr //= 10
	if digit_sum == i:
		total.append(digit_sum)
print(sum(total))