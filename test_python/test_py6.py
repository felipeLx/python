# valid anagram
def v_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq1 = {}
    freq2 = {}

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True

# using Library
from collections import Counter

from pyrsistent import T

def are_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

# using sorted
def are_anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


# find the index of the first and last position of target in arr
def first_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1, 1]

# using binary research
def find_start(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr)-1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

def first_and_last(arr, target):
    if len(arr) == 0 \
    or arr[0] > target \
    or arr[-1] < target:
        return [-1, 1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]

# kth largest element
def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

# with sorted
def kth_larg_sorted(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

# with heap
import heapq
def kth_larg_heap(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    
    return -heapq.heappop(arr)

# check if binarytree are simetric
def are_sym(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_sym(root1.left, root2.right) \
            and are_sym(root1.right, root2.left)

def is_sym(root):
    if root is None:
        return True
    return are_sym(root.left, root.right)

# check parantesis
def is_Vald(combination):
    stack=[]
    for par in combination:
        if par == '(':
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

# choose the cheaper solution
def can_traverse(gas, cost, start):
    n = len(gas)
    remaining = 0
    i = start
    started = False
    while i !=start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i+1)%n
    return True

def gas_station(gas, cost):
    remaining = 0
    candidate = 0

    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i+1
            remaining = 0
    prev_remaining = sum(gas[:candidate]) - sum(cost[:candidate])
    if candidate == len(gas) or remaining+prev_remaining < 0:
        return -1
    else:
        return candidate

from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        ranks = [(-counter['score'], counter['games_played'], i, name)
        for i, (name, counter) in enumerate(self.standings.items())]

        return sorted(ranks)[rank-1][3]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))