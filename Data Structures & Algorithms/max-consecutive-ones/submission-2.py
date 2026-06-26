class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                if(x < temp):
                    x = temp
                temp = 0

            if(x<temp):
                x = temp
        return x