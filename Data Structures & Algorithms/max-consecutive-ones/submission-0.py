class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        longest = 0
        for num in nums:
            if (num == 1):
                m += 1
                if m >= longest:
                    longest = m
            else:
                m = 0
        return longest