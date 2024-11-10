class Solution:
    # Function to sort an array of 0s, 1s, and 2s using the Dutch National Flag Algorithm
    def sort012(arr):
        n = len(arr)
        lo = 0
        hi = n - 1
        mid = 0
    
        # Iterate till all the elements are sorted
        while mid <= hi:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi -= 1
    
        return arr
    
    # Example usage
    arr = [0, 1, 2, 0, 1, 2]
    arr = sort012(arr)
    
    # Output the sorted array
    for x in arr:
        print(x, end=" ")

        