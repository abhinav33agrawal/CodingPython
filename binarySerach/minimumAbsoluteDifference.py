def minimumDifference(arr, key):
    start = 0
    end = len(arr)-1
    floor = -1
    ceil = -1
    while start <= end:
        mid = start+((end-start)//2)
        if arr[mid] == key:
            return key
        elif arr[mid] > key:
            end = mid-1
            ceil = arr[mid]
        else:
            start = mid+1
            floor = arr[mid]
    print(floor, ceil)
    print(start, end)
    if abs(key-floor) < abs(key-ceil):
        return floor
    else:
        return ceil


arr = [1, 3, 8, 10, 15]
key = 12
print(minimumDifference(arr, key))
