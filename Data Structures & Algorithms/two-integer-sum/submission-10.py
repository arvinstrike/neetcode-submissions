class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = sorted(nums) janga di sort karena indexnya nanti berubah
        seen = {}

        for i in range(len(nums)):
            butuh = target - nums[i]
            if butuh in seen:
                return [seen[butuh],i]
                
            seen[nums[i]] = i
                


            
        