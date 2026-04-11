from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        grp = defaultdict(list)

        for word in strs:

            freq = Counter(word)
            key = tuple(sorted(freq.items()))
            grp[key].append(word)
        
        return list(grp.values())

            

        
