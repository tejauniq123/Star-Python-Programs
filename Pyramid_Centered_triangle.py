n = 5
for i in range(1, n+1):
    spaces = ' ' * (n - i)      # left padding
    stars  = '*' * (2*i - 1)    # odd number of stars
    print(spaces + stars)