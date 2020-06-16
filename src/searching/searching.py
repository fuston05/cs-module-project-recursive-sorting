# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # base case
    # when start passes end
    if start > end:
        return -1

    # initialize a mid index var
    mid = (start+end) // 2

    # if target == mid, then we have a match, return mid
    if target == arr[mid]:
        return mid
    # else if target is less than mid, move start up to mid
    elif target < arr[mid]:
        end = mid-1
    # else.. target is greater than mid, move end down to mid+1
    else:
        start = mid+1
    return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
