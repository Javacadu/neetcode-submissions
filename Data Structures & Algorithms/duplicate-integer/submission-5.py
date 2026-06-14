class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # retun true if val is already in array, else return false
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False
        