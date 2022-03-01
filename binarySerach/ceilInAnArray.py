def findCeil(arr, target):
    start = 0
    end = len(arr)-1
    res = -1

    while start <= end:
        mid = start+int((end-start)/2)
        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            res = arr[mid]
            end = mid-1
        else:
            start = mid+1

    return res


arr = [1, 2, 8, 10, 10, 12, 19]
target = 4
print(findCeil(arr, target))
