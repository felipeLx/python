# give a list, check if the second argument is present in the list

def matcher(list, match):
    for item in list:
        if item == match:
            return True
        return False

# Array sequence
#  List []
#  Tupple (,)
#  String ("") ** all supporting index

import sys
n = 5
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(n)

# fiven two strings, check to see if they are anagrams
def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

print(anagram('God', 'doggy'))

def anagram_dic(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

x = anagram_dic('Clint Eastwood', 'old WEST action')
print(x)

# given an integer array, output all the unique pairs that sum up to a specific value k
def pair_sum(array, k):
    if len(array) < 2:
        print('small array')
    
    seen = set()
    output = set()

    for num in array:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    
    print('\n'.join(map(str, list(output))))

pair_sum([3,3,5,1], 6)

# array with positive and negative integers and find the maximum sum of the array
def largest(arr):
    if len(arr) == 0:
        return print('to small')
    
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)

    return max_sum

# reverse a string
# start: "This is the best"
# finish: "best the is This"
def reverse(str):
    return " ".join(reversed(str.split())) 
    # return " ".join(str.split()[::-1])

# reverse all letter of the string
def reverseall(s):
    length = len(s)
    spaces = [" "]
    words = []
    i = 0
    while i < length:
        if s[i]not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])
        
        i += 1
    
    return "".join(reversed(s))
print(reverseall('Python is the best'))

# given 2 arrays(assume no duplicates)
# find the same element in list2 and check index for index from there
def rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    key = list1[0]
    key_counter = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break
    
    if key_index == 0:
        return False
    
    for x in range(len(list1)):
        l2index = (key_index + x) % len(list1)

        if list1[x] != list2[l2index]:
            return False
    return True

print(rotation([1,2,3,4,5,6], [4,5,6,1,2,3]))

# common elements in two sorted arrays
def common(arr1, arr2):
    p1 = 0
    p2 = 0
    res = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1
        else:
            p1 += 1
    return res

print(common([1,2,3,4,5,6,7], [4,5,6,9,10,11]))

# function with 3 arguments
def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb_loc in bombs:
        (bomb_row, bomb_col) = bomb_loc
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            for j in col_range:
                if(0 <= i < num_rows and 0 <= j < num_cols and field[i][j]!= -1):
                    field[i][j] += 1
    return field


print(mine_sweeper([[0,0], [1,2]], 3, 4))

# unique characters
def unique(s):
    s = s.replace(' ','')
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True

# first no repeat element in array
def non_repeting(string):
    string = string.replace(' ', '').lower()
    char_count = {}

    for c in string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    
    for c in string:
        if char_count[c] == 1:
            return c
    
    return None

# all no repeat element in array
def all_non_repeting(string):
    string = string.replace(' ', '').lower()
    char_count = {}

    for c in string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    all_unique = []
    y = sorted(char_count.items(), key=lambda x: x[1])

    for item in y:
        if item[1] == y[0][1]:
            all_unique.append(item)
    
    return all_unique

print(all_non_repeting('I love to eat hamburger from McDonald'))