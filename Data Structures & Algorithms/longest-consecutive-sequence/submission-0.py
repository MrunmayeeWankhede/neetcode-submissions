class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort the array to check
        my_list = sorted(nums)
        #remove duplicates
        unique_list = list(dict.fromkeys(my_list))
        #create the best vaue (longest substring)
        best = 0
        #create the total length at a particular point
        #this would be 1 not 0
        #this is because when the loop conditional is true:
        #at that point there will be 2 elements in consecutive order
        total = 1
        #loop over the elements
        for i in range(len(unique_list)):
            if unique_list[i] == unique_list[i-1] + 1:
                total += 1
            else:
                total = 1
            if total > best:
                best = total
        return best

        