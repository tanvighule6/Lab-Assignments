def count_ways(coins, amount):
    # dp[i] = number of ways to make amount i
    dp = [0] * (amount + 1)

    # There is one way to make amount 0: use no coins
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


# Accept coin denominations
coins = list(map(int, input("Enter coin denominations: ").split()))

# Accept target amount
amount = int(input("Enter target amount: "))

# Calculate and display result
ways = count_ways(coins, amount)

print("Total possible combinations:", ways)

#INPUT
Enter coin denominations: 1 2 5
Enter target amount: 5
#OUTPUT
Total possible combinations: 4
