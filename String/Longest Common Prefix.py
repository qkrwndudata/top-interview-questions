# 링크: https://leetcode.com/problems/longest-common-prefix/ -> Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        for i, v in enumerate(strs[0]):
            for j in strs:
                if j[i] != v:
                    return strs[0][:i]
        return strs[0]
    
    
# zip을 배워 감
