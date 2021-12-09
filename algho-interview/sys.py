import sys
n = 10
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)

    print('length: {0:3d}; size bites: {1:4d}'.format(a,b))

    data.append(n)

    # given 2 strings, check if they are anagrams.
    def anagram(s1, s2):
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
        # return sorted(s1) == sorted(s2)
    

    
