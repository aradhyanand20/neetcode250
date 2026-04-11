class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()

        for word in strs:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end = True
        
        prefix = ""
        node = root
        while len(node.children) == 1 and node.end == False:
            ch = list(node.children.keys())[0]
            prefix += ch
            node = node.children[ch]
        
        return prefix