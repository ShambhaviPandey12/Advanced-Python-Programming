# A person can climb 1 or 2 stairs at a time.
# Find total ways to reach the top.

def stairs_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = stairs_memo(n - 1, memo) + stairs_memo(n - 2, memo)
    return memo[n]


def stairs_table(n):
    table = [0] * (n + 1)
    table[0] = 1
    if n >= 1:
        table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


steps = 6

print("Ways to climb using Memoization:", stairs_memo(steps))
print("Ways to climb using Tabulation:", stairs_table(steps))

#Output
'''Ways to climb using Memoization: 13
Ways to climb using Tabulation: 13'''