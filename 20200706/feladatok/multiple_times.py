# Adott egy egész számokból álló lista. Ha legalább egy elem kétszer szerepel a listában,
# akkor a visszatérési értékünk igaz, ha minden elem különböző, azaz csak egyszer szerepel a listában,
# akkor visszatérési értékünk hamis lesz.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [3, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums4 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def multiple_times(nums):
    for i in nums:
        if nums.count(i) >= 2:
            print('true')
            return
        else:
            nums.count(i) < 2
            print('false')

        return


multiple_times(nums4)
