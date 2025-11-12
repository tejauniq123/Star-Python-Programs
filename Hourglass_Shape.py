n = 5
# Upper half (inverted pyramid)
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))

# Lower half (regular pyramid, skip middle)
for i in range(2, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))