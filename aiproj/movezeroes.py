class Solution:
    def moveZeroes(self, nums):
        left = 0  # Pointer to track where to place the next non-zero element

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


'''
def moveZeroes(nums):
    left = 0  # Pointer to track where to place the next non-zero element

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

# Example test cases
if __name__ == "__main__":
    nums1 = [0, 1, 0, 3, 12]
    moveZeroes(nums1)
    print(nums1)  # Output: [1, 3, 12, 0, 0]

    nums2 = [0]
    moveZeroes(nums2)
    print(nums2)  # Output: [0]

    nums3 = [4, 0, 5, 0, 6, 0, 7, 8]
    moveZeroes(nums3)
    print(nums3)  # Output: [4, 5, 6, 7, 8, 0, 0, 0]

    nums4 = [1, 2, 3, 4, 5]
    moveZeroes(nums4)
    print(nums4)  # Output: [1, 2, 3, 4, 5]

    nums5 = [0, 0, 0, 0, 0]
    moveZeroes(nums5)
    print(nums5)  # Output: [0, 0, 0, 0, 0]
