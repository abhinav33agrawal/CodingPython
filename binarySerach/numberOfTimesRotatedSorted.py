def numberOfTimes(arr, target=0):
    start = 0
    N = len(arr)
    end = N-1
    while start <= end:
        print(start, end)
        mid = start + int((end-start)/2)
        next_ = (mid+1) % N
        print('next_: ', next_)
        previous = (mid+N-1) % N
        print('previous: ', previous)
        # print(next_, previous)
        # print('arr[mid] <= arr[next_]: ', arr[mid] <= arr[next_])
        # print('arr[mid] >= arr[previous]: ', arr[mid], arr[previous])
        if arr[mid] <= arr[next_] and arr[mid] <= arr[previous]:
            return mid
        else:
            firstArray = True if arr[mid] >= arr[start] else False
            print('firstArray: ', firstArray)
            secondArray = True if arr[mid] <= arr[end] else False
            print('secondArray: ', secondArray)
            if firstArray and not secondArray:
                start = mid+1
            elif not firstArray and secondArray:
                end = mid-1
            elif firstArray and secondArray:
                return start


arr = [7, 9, 11, 12, 5]
print(numberOfTimes(arr))
'''
Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0
'''
