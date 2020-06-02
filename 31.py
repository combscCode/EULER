'''
Coin Sums

dynamic programming problem
'''

def first_find_num_solutions(coins, total):
	# DP problem
	ways = [[-2 for i in range(total)] for j in range(len(coins))]

	to_process_queue = [(len(coins)-1, total-1)]
	ways[len(coins)-1][total-1] = -1
	while len(to_process_queue):
		c, t = to_process_queue[0]
		to_process_queue.pop(0)
		while c > 0 and t >= 0:
			ways[c-1][t] = -1
			to_process_queue.append((c-1,t))
			t -= coins[c]
	for t in range(total):
		for c in range(len(coins)):
			if ways[c][t] != -2:
				to_add = 0
				if (t+1) % (coins[c]) == 0:
					to_add += 1
				if c > 0:
					var_c = c
					var_t = t
					while var_t >= 0:
						to_add += ways[var_c-1][var_t]
						var_t -= coins[var_c]
				ways[c][t] = to_add
	return ways[c][t]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200
def second_find_num_solutions(c, t):
	if c == 0:
		return 1
	ways = 0
	while t >= 0:
		ways += second_find_num_solutions(c-1, t)
		t -= coins[c]
	return ways

coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200
memo = [[0 for i in range(total+1)] for j in range(len(coins))]
def third_find_num_solutions(c, t):
	if memo[c][t] > 0:
		return memo[c][t]
	if c == 0:
		memo[c][t] = 1
		return 1
	ways = 0
	while t >= 0:
		ways += second_find_num_solutions(c-1, t)
		t -= coins[c]
	memo[c][t] = ways
	return ways

if __name__ == '__main__':
	#coins = [1,2,3]
	#x = first_find_num_solutions(coins, total)
	#x = second_find_num_solutions(len(coins)-1, total)
	x = third_find_num_solutions(len(coins)-1, total)
	print(x)