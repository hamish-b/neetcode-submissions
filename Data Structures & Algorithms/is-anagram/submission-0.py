class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_table_s = [0 for _ in range(26)]
        hash_table_t = hash_table_s.copy()

        def to_index(letter):
            index = ord(letter) - 97
            return index

        def hash_function(word, hash_table):
            indexes = []
            for letter in word:
                indexes.append(to_index(letter))    
            
            for i in indexes:
                hash_table[i] += 1
            return hash_table

        if hash_function(s, hash_table_s) == hash_function(t, hash_table_t):
            return True
        else:
            return False