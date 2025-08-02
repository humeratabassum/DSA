#default dict is used to store group of anagrams
#defaultdict(list) automatically creates a list when a new key is used 

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for word in strs:
            key=tuple(sorted(word))
            groups[key].append(word)
        return list(groups.values())   


        # anagram_map=defaultdict(list)

        # for word in strs:
        #     key=''.join(sorted(word))
        #     anagram_map[key].append(word)
        # return list(anagram_map.values())


""" it is in the form of key value pairs
{
  "aet": ["eat", "tea", "ate"],
  "ant": ["tan", "nat"],
  "abt": ["bat"]
}
"""
"""
| Word | Sorted Letters   | Key   |
| ---- | ---------------- | ----- |
| eat  | \['a', 'e', 't'] | "aet" |
| tea  | \['a', 'e', 't'] | "aet" |
| tan  | \['a', 'n', 't'] | "ant" |
| ate  | \['a', 'e', 't'] | "aet" |
| nat  | \['a', 'n', 't'] | "ant" |
| bat  | \['a', 'b', 't'] | "abt" |
"""
