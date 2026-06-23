class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        x = 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                temp = 0
            if temp > x:
                x = temp
        return x