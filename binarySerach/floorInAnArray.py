def findFloor(arr, target):
    start = 0
    res = -1
    end = len(arr)-1
    while start <= end:
        print(start, end)
        mid = start + int((end-start)/2)
        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            res = arr[mid]
            start = mid+1
        else:
            end = mid-1
        print(start, end)
    return res


arr = [1, 2, 8, 10, 10, 12, 19]
target = 4
print(findFloor(arr, target))
