def findPeak(arr):
    start = 0
    end = len(arr)-1
    if len(arr) == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return 0

    while start <= end:
        # print(start, end)
        mid = start+(end-start)//2
        # print(start, end, mid)
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return mid
        if arr[mid] > arr[mid+1]:
            end = mid-1
        else:
            start = mid+1


def BinarySearch(arr, target):
    start = 0
    end = len(arr)-1
    reverse = 1 if start <= end else -1
    while start <= end:

        mid = start + int((end-start)/2)

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-reverse
        else:
            start = mid+reverse


def findElement(arr, target):
    peak = findPeak(arr)
    arr1 = BinarySearch(arr[peak:], target)
    print('arr1: ', arr1, arr[peak:])
    arr2 = BinarySearch(arr[:peak], target)
    print('arr2: ', arr2, arr[:peak])

    if arr1 == -1 and arr1 == -1:
        return -1
    if arr1 != -1:
        return peak+arr1

    else:
        return arr2-1


arr = [1, 2, 3, 8, 3, 2, 1, 0]

print(findElement(arr, 2))
