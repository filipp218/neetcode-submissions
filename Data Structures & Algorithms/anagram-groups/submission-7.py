class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_group_anagram = dict()

        for i in range(len(strs)):
            word = strs[i]
            key_list = sorted(list(word))
            sorted_key = ''.join(key_list)

            dict_group_anagram.setdefault(sorted_key, [])
            dict_group_anagram[sorted_key].append(i)
        
        result = []
        for value in dict_group_anagram.values():
            result.append([strs[val] for val in value])
        
        return sorted(result, key=lambda x: len(x))