# 링크: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# 문제 설명: 주어진 string('heystack')에 특정 string('needle')이 어느 위치에 있는지를 반환하되, 없으면 -1을 반환

# 내 풀이: map을 활용하여, haystack을 뒤에서부터 needel의 길이만큼 단어를 확인해 가며 index와 해당하는 단어를 word라는 dictionary에 저장 -> needle을 해당 map에서 찾음
## 피드백: map을 사용하기 때문에 memory 측면에서 비효율적. 시간은 괜찮음
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        words = {}
        for i in reversed(range(len(haystack)-len(needle)+1)):
            words[haystack[i:(i+len(needle))]] = i
        if needle in words:
            return words[needle]
        else:
            return -1
        
# 다른 풀이: string의 index는 string 맨 앞 글자의 index임을 활용
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack : 
						return (haystack.index(needle))
        else: return -1
