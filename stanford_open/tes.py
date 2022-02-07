def test(init, end, tup):
    n_tup = str(tup[init:end])
    return '"' + n_tup + '"'

print(test(1,3,(12,14,13,11,14,11)))