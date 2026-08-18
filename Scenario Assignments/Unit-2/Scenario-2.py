def fibonacci(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


# Accept N
n = int(input("Enter N: "))

# Generate Fibonacci sequence
dp = fibonacci(n)

# Display sequence
print("Fibonacci sequence:")
for i in range(n + 1):
    print(dp[i], end=" ")

#Sample Input
#Enter N: 7
#Sample Output
#Fibonacci sequence:
#0 1 1 2 3 5 8 13
