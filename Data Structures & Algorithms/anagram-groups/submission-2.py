from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grp = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for ch in word:
                freq[ord(ch)- ord('a')] +=1

            grp[tuple(freq)].append(word)

        return  list(grp.values())

            

         