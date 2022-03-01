def nearbySearching(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        print(start, end)
        mid = start + int((end-start)/2)
        if arr[mid] == target:
            return mid
        if mid+1 <= end and arr[mid+1] == target:
            return mid+1
        if mid-1 >= start and arr[mid-1] == target:
            return mid-1

        print('arr[mid]: ', arr[mid])
        if arr[mid] < target:
            start = mid+2
        else:
            end = mid-2

    return -1


arr = [10, 3, 40, 20, 50, 80, 70]
target = 1
print(nearbySearching(arr, target))
