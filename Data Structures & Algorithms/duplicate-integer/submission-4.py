class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenData = set()

        for num in nums:
            if num in seenData:
                return True
            seenData.add(num)

        return False