from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        freq=Counter(s)
        sorted_char = sorted(freq.keys() , key=lambda x:-freq[x])
        return "".join(char*freq[char] for char in sorted_char)

        