# returns the highest possible next_val st when we get to the end we
# won't go over the target_sum
def max_next_val_careful(sum_val, n):
    # sum_val = x + (x + 1) + ... + (x + n - 1)
    # sum_val = xn + (n-1)(n)//2
    # x = (sum_val - (n-1)(n)//2)//n
    # quick maths
    return (sum_val - (n-1) * n // 2) // n

# Return either the augmented subset sums set, or return None if a repeat would occur
def get_new_subset_sums(subset_sums, next_val):
    new_subset_sums = set(subset_sums)
    for s in subset_sums:
        if s + next_val in new_subset_sums:
            return None
        new_subset_sums.add(s + next_val)
    return new_subset_sums

def search(sum_val, n, current = [], subset_sums = {0}):
    if n == 1:
        if current and sum_val < current[-1]:
            return None
        new_subset_sums = get_new_subset_sums(subset_sums, sum_val)
        if new_subset_sums is None:
            return None
        solution = current + [sum_val]
        if sum(solution[:(len(solution) + 1) // 2]) > sum(solution[len(solution) // 2 + 1:]):
            return solution
        return None

    start = current[-1] + 1 if current else 1
    if len(current) - n in (-1, 0):
        # Want sum(current) + start > sum_val - start
        # start = (sum_val - sum(current)) // 2
        start = max(start, (sum_val - sum(current)) // 2)

    for next_val in range(start, max_next_val_careful(sum_val, n) + 1): #careful
        new_subset_sums = get_new_subset_sums(subset_sums, next_val)
        if new_subset_sums is None:
            continue
        solution = search(sum_val - next_val, n - 1, current + [next_val], new_subset_sums)
        if solution is not None:
            return solution
    return None

n = 7
sum_val = (n * (n + 1)) // 2
while True:
    solution = search(sum_val, n)
    if solution is not None:
        break
    sum_val += 1
for s in solution:
    print(s, end='')
print()