class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = sorted(nums) janga di sort karena indexnya nanti berubah

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # if nums[i] == nums[j]: ini salah pahamin soal, indexnya yg ga boleh sama bukan nilainya
                #     break
                if nums[i] + nums[j] == target:
                    if nums[i] < nums [j]:
                        nums[i], nums[j] = nums[j], nums[i]
                    return [i,j]


            
        