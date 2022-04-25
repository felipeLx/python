# permutation, discover all possible combination from lists
import itertools
import pandas as pd

list_opt = [[1],[2,3],[4,5],[6,7],[8],[9,10],[11],[13,14],[15],[16,17,18],[19],[20,21],[22,23],[24],[25]]

list_result = list(itertools.product(*list_opt))
df = pd.DataFrame(list_result)
df.to_csv('permutation.csv', index=False, header=False)
print(df.head())
""""
list1 = [1]
list2 = [2,3]
list3 = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25]
list3 = [3,4,5]
list4 = [6,7]
list5 = [7,8]
list6 = [9,10]
list7 = [10,11]
list8 = [13,14]
list9 = [14,15]
list10 = [16,17,18]
list11 = [17,18,19]
list12 = [19,20,21]
list13 = [21,22,23]
list14 = [23,24]
unique_combination = []
permut = list(itertools.permutations(list3, 15))
print(permut)
list15 = [25]
"""
"""
for comb in permut:
    zipped = 
"""