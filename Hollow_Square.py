n = 5
for i in range(n):
    if i == 0 or i == n-1:           # top & bottom
        print('*' * n)
    else:                            # middle rows
        print('*' + ' '*(n-2) + '*')