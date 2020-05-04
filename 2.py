'''
NOTES
Find the sum of the even valued terms of fib sequence up to some value

fib sequence:
Fn = Fn-1 + Fn-2

1,2,3,5,8,13,21,34...

even valued terms:
2,5,13,34

Just calculate keeping a running sum until value exceeds max_val
To reduce copying we're going to alternate which val (a or b) we overwrite
'''

max_val = 4e6
running_sum = 2
current_val = 3
val_a = 2
val_b = 1
while current_val <= max_val:
	if current_val % 2 == 0:
		running_sum += current_val
	val_b = val_a
	val_a = current_val
	current_val = val_a + val_b
	print(current_val)
print(running_sum)
