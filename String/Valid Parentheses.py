# 링크: https://leetcode.com/problems/valid-parentheses/
# 문제 설명: 괄호((, {, [)가 잘 사용되었는지 확인하는 문제

## 내 풀이: stack 사용

class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in match:
                if len(stack) == 0:
                    return False
                else:
                    t = stack.pop()
                    if t != match[i]:
                        return False
        return len(stack) == 0
