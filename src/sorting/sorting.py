# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, count= 0):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # use count to track index for merged_arr insertions
    
    # **** this is a mess, I am aware that this can be refactored, ill try
    # - to come back and clean this up later ****
    count= 0
    while count != elements:
        # if arrA gets emptied before B?
        if len(arrA) > 0 and not len(arrB) > 0:
            for i in arrA:
                merged_arr[count]= i
                count+=1
        # if arrB gets emptied before A?
        elif len(arrB) > 0 and not len(arrA) > 0:
            for i in arrB:
                merged_arr[count]= i
                count+=1
        # both A and B still have elements
        else:
            # if a is bigger
            if arrA[0] > arrB[0]:
                # add b to merged_arr
                merged_arr[count]= arrB[0]
                arrB.pop(0)
                count+=1
            # if B is bigger
            else:
                # add a to merged_arr
                merged_arr[count]= arrA[0]
                arrA.pop(0)
                count+=1
            # increment count
        
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):
    if len(arr) > 1:
        splitPoint = len(arr)//2
        left= arr[:splitPoint] 
        right= arr[splitPoint:] 
        return merge(merge_sort(left), merge_sort(right))
        
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
