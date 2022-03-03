c = [[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50]]


def matrixSearcrch(arr, target):
    m = len(c)-1
    n = len(c[0])-1
    i = 0
    j = n
    while i >= 0 and j >= 0 and i <= m and j <= n:
        print(i, j)
        if target == arr[i][j]:
            return i, j
        elif arr[i][j] > target:
            j -= 1
        else:
            i += 1
    return -1


# matrixSearcrch(c, 25)
print('matrixSearcrch(c, 25): ', matrixSearcrch(c, -1))
