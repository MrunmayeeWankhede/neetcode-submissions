class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create an empty dictionary
        my_dict = {}
        #loop over the words in the list
        for word in range(len(strs)):
            #convert to tuple, lists are not hashable
            #these would serve as our keys
            #keys would have anagrams as their value
            sorted_words = tuple(sorted(strs[word]))
            #if key not in dictionary, add key and its value
            if sorted_words not in my_dict:
                my_dict[sorted_words] = [strs[word]]
            #if key alr there, just add the value
            else:
                my_dict[sorted_words] += [strs[word]]

        return list(my_dict.values())


        