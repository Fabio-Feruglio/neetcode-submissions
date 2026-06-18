class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0

        for c in numSet:
            if (c-1) not in numSet:
                lenght=1
                while (c+lenght) in numSet:
                    lenght+=1
                longest=max(lenght,longest)
        return longest
            