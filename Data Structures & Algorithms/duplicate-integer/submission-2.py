class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}

        for c in nums:

            if c in seen:
                return True
            seen[c]=1

        return False