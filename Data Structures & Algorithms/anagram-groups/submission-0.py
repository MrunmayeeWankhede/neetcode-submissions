class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in range(len(strs)):
            sorted_words = tuple(sorted(strs[word]))
            if sorted_words not in my_dict:
                my_dict[sorted_words] = [strs[word]]
            else:
                my_dict[sorted_words] += [strs[word]]

        return list(my_dict.values())


        