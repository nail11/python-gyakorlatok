# Adott egy egész számokból álló lista. Egy elem kivételével, minden elem kétszer fordul elő a listában.
# Keresd meg melyik az az elem, ami csak egyszer szerepel a listában.
# Example 1:
# Input: nums =
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

def single_number(nums):
    for i in nums:
        if nums.count(i) == 1:
            print('Ez az elem szerepel egyszer a listában: ' + str(i))


nums1 = [2, 2, 1, ]
nums2 = [4, 1, 2, 1, 2]
nums3 = [2, 3, 3, 4, 5, 2]

single_number(nums3)
