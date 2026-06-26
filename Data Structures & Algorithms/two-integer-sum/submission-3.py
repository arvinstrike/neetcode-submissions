class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = sorted(nums) janga di sort karena indexnya nanti berubah
        seen = {}

        for i in range(len(nums)):
            butuh = target - nums[i]
            if butuh in seen:
                if i > seen[butuh]:
                    return [seen[butuh],i]
                return [i,seen[butuh]]
            seen[nums[i]] = i
                


            
        