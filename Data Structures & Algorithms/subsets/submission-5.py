class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        partial = []
        def subsetRecur(counter):
            if counter >= len(nums):
                result.append(partial.copy())
                return
            partial.append(nums[counter])
            subsetRecur(counter + 1) 
            partial.pop()
            subsetRecur(counter + 1)
        subsetRecur(0)
        return result
        