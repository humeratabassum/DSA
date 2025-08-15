from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False

# 2. Check if both strings use the same set of characters.
        if set(word1)==set(word2):
# 3. Count the occurrences (frequency) of each character.

            count1,count2=Counter(word1),Counter(word2)
            return sorted(count1.values()) == sorted(count2.values())
        return False
     # 4. The frequency distribution must be the same (sorted, so order doesn't matter).
        