# print all values from a list
def func_lin(lst):
    for val in lst:
        print(val)

def comp(lst):
    print(lst[0])
    midpoint = len(lst)//2

    for val in lst[:midpoint]:
        print(val)
    
    for x in range(10):
        print('number')

lst = [1, 2, 3]
func_lin(lst)