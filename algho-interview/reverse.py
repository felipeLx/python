# string of words, reverse
def reverse_string(s):
    return "-".join(reversed(s.split()))

def rev(s):
    return s.split()[::-1]

# given 2 arrays, no duplicate. Select and indexed position in listl and gets its value.
def rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    key = list1[0]
    key_index = 0

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

print(rotation([1,2,3,4,5], [5,4,3,2,1]))