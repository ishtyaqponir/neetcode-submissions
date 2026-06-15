class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums is None:
            return false
        s = set()
        for i, x in enumerate(nums):
            if x in s:
                return True
            else:
                s.add(x)
        return False
        