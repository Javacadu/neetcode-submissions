class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # retun true if val is already in array, else return false

        return len(nums) != len(set(nums))