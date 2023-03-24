# 링크: https://leetcode.com/problems/plus-one/
# 문제 설명: 정수 리스트가 주어지면 만들어지는 하나의 수에 1을 더한 값을 정수 리스트로 반환   ex) [1, 2, 3] -> [1, 2, 4]

# 내 풀이: join을 사용해 리스트를 문자 -> 정수 -> 문자 순으로 처리해 리스트로 반환
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        s = ''.join([str(n) for n in digits])
        new = str(int(s) + 1)
        for i in new:
            answer.append(int(i))

        return answer
    
# 다른 풀이: map 함수를 사용하면 더 빠른 동작이 가능
class Solution(object):
    def plusOne(self, digits):
        digits = list(map(str, digits))
        digits = "".join(digits)
        ans = int(digits) + 1
        result = list(str(ans))   # list(str())
        return list(map(int, result))
