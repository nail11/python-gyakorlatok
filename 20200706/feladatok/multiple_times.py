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


nums = [1, 2, 3, 4]


def multiple_times(nums):
    for i in nums:
        if nums.count(nums[i]) >= 2:
            print('true')
            return
        elif nums.count(nums[i]) < 2:
            print('false')
            i += 1
        return


multiple_times(nums)
