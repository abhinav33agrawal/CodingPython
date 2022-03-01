def firstAndLast(arr, target, first):
    start = 0
    res = -1
    end = len(arr)-1
    reverse = 1 if start <= end else -1
    while start <= end:

        mid = start + int((end-start)/2)

        if arr[mid] == target:
            res = mid
            if first:
                end = mid-1
            else:
                start = mid+1
        elif arr[mid] > target:
            end = mid-reverse
        else:
            start = mid+reverse

    return res


arr = [1, 4, 5, 6, 6, 6, 6, 7, 8, 9]
target = 6
print(firstAndLast(arr, target, True))
print(firstAndLast(arr, target, False))
