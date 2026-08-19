class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #make an empty set
        seen = set()
        for i in nums:
            if i in seen:
                return True
            #keep adding the numbers in the set
            seen.add(i)
        return False