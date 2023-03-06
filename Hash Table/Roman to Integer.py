# 링크: https://leetcode.com/problems/roman-to-integer/

### 내 답안 ###

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}   # dict1 
        subs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}   # dict2: 빼줘야 하는 연산을 미리 연산해 dictionary로 저장
        i = 0   # while문 초기치
        answer = 0   # output을 저장할 공간

        while i < len(s):   # 주어진 문자열 s의 길이만큼 순환
            if (i+1) != len(s) and s[i] + s[i+1] in subs.keys():   # 인덱스 i가 문자열의 길이를 넘지 않고 문자열의 연속된 조합이 dict2에 위치해 있을 경우
                sub = subs[s[i] + s[i+1]]   # dict2에서 대응되는 값 sub에 저장하고
                answer += sub   # answer에 더해줌
                i += 2   # index는 두 칸 건너 뜀
            else:   # 문자열의 연속된 조합이 dict2에 위치해 있지 않을 경우
                answer += roman[s[i]]   # dict1에서 대응되는 값을 answer에 더해줌
                i += 1   # index는 한 칸 건너 뜀
        return answer   # answer 반환

### 모범 답안 1###
https://leetcode.com/problems/roman-to-integer/solutions/264743/clean-python-beats-99-78/?orderBy=most_votes

class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0   # output을 저장할 공간

        # 변수.replace(old, new)
        s = s.replace("IV", "IIII").replace("IX", "VIIII")   
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

### 모범 답안 2 ### 
https://leetcode.com/problems/roman-to-integer/solutions/450264/python-beginner-98-fast-100-memo/?orderBy=most_votes
    
def romanToInt(self, s: str) -> int:
	res, prev = 0, 0
	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	for i in s[::-1]:          # rev the s
		if dict[i] >= prev:
			res += dict[i]     # sum the value iff previous value same or more
		else:
			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
		prev = dict[i]
	return res
