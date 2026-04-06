class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) == len(t):
            for ch, ch2 in zip(s,t) :
              dict1[ch] = dict1.get(ch,0)+1
              dict2[ch2] =dict2.get(ch2,0)+1

            if dict1 == dict2 :
              return True
        return False



