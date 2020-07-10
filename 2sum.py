from utils.hashtable import HashTable

class Solution(object):
    def __init__(self):
        self.values = HashTable()

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        for num in nums:
            remainder = target - num
            remainder_index = self.values.get_val(remainder)
            if remainder_index is not None and remainder_index != i:
                    return [remainder_index, i]
            self.values.set_val(num, i)
            i = i + 1

        return None


s = Solution()
ans = s.twoSum([1, 2], 3)
print(ans)
