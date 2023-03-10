# 링크: https://leetcode.com/problems/longest-common-prefix/ -> Write a function to find the longest common prefix string amongst an array of strings. 
# If there is no common prefix, return an empty string `""`

### 내 풀이 ###
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        for i, v in enumerate(strs[0]):
            for j in strs:
                if j[i] != v:
                    return strs[0][:i]
        return strs[0]
    
    
### 모범 답안: zip()과 set()을 사용해 비교
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))   # *strs: 문자열을 가장 최소 단위로 쪼갬 -> zip(): 튜플로 묶어줌
        prefix = ""
        for i in l:
            if len(set(i))==1:   # 튜플로 묶인 각 문자가 전부 동일하면 set의 길이는 1 -> ex. (f, f, f)
                prefix += i[0]
            else:
                break
        return prefix
