def largestRange(array):
    numbers = {x:0 for x in array}
    left = right = 0

    for number in array:
        if numbers[number]== 0:
            left_count = number -1
            right_count = number +1

            while left_count in numbers:
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1

            if(right - left) <= (right_count - left_count):
                right = right_count
                left = left_count
    return [left, right]


# print(largestRange([1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]))

# take an input of n and return the sum of the numbers from 0 to n
def sum(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

# print(sum(8))

def sum2(n):
    return (n*(n+1))/2

print(sum2(8))