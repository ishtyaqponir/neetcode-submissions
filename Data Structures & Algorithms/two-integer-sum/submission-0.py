class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or target == None:
            return []
        hashMap = dict()
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i

        
        