class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        all_dict={}
        for i,num in enumerate(nums):
            if num in all_dict:
                return True
            all_dict[num]=i
        return False
        