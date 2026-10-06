class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def to_index(letter):
            return ord(letter) - 97
        
        hash_map = {}

        # want key to be a sorted list of values corresponding to letters
        # so for example "and" and "dan" would be {[1, 4, 14]: ["and", "dan"]}

        def to_sorted_list(word):
            word_list = [to_index(letter) for letter in word]
            word_list.sort()
            return str(word_list)

        for word in strs:
            sorted_word = to_sorted_list(word)
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]

        return list(hash_map.values())