class Solution:
    def binarysearch(self, arr, k):
        # Initialize the left and right pointers
        left, right = 0, len(arr) - 1
        
        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index
            
            # Check if k is at mid
            if arr[mid] == k:
                return mid  # Return the index if found
            elif arr[mid] < k:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        
        return -1  # Return -1 if k is not found

# Example usage
solution = Solution()
print(solution.binarysearch([1, 2, 3, 4, 5], 4))  # Output: 3
print(solution.binarysearch([11, 22, 33, 44, 55], 445))  # Output: -1