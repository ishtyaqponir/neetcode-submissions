class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = sorted(set(nums))
        nums[:len(numSet)] = list(numSet)
        return len(numSet)
        