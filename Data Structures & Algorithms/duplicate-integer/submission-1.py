class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # retun true if val is already in array, else return false

        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)

        return False