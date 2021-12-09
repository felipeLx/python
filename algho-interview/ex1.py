# Take an input and return the sum
def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

sum1(5)

def sum2(n):
    return (n*(n+1))/2

sum2(5)

# to compare wich is more fast
# %timeit sum1(100)
# %timeit sum2(100)

# Big-O analysis is also know as asymptotic analysis = describing limiting behavior
def Bigo(n):
    return 45*n**3 +20*n**2 + 19

Bigo(1) # 19 not will be a scaling or limiting factor


