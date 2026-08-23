class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a hashmap matching sorted order of word to a list 
        # logic... if sorted word not in hashmap match its key to a list with just itself 
        # if sorted key present add to that same list

        sortedkey_list = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in sortedkey_list:
                sortedkey_list[key] = [strs[i]]
            else:
                sortedkey_list[key].append(strs[i])

        return list(sortedkey_list.values())