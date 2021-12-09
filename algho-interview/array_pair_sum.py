def pair_sum(array, k):
    if len(array) < 2:
        return print('Small array')
    
    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    
    print('\n'.join(map(str, list(output))))

pair_sum([1,3,2,2], 4)

# Find the Max Sum
def largest(arr):
    if len(arr) == 0:
        print('Array to small')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    
    return max_sum

print(largest([7,1,2,-1, 3, 4 -12, 3, -19]))