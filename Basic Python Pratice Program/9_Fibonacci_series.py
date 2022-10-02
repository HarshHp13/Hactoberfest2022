# To get the nth element of the fibonacci sequence
dp=[0, 1]

def fibonacci(n):
    if n<0:
        print("Enter a valid input!!!")
    elif n<len(dp):
        return dp[n]
    else:
        dp.append(fibonacci(n-2)+fibonacci(n-1))
        return dp[n]

a=int(input())
print(fibonacci(a))