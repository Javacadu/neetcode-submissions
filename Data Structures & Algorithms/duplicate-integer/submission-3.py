class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # retun true if val is already in array, else return false

        return len(set(n for n in nums)) != len(nums)