# 링크: https://leetcode.com/problems/sqrtx/
# 문제 설명: 지수를 사용하지 않고 제곱근 값을 구해라

# 내 풀이: 최악의 풀이 ->  linear search를 사용했음

class Solution:
    def mySqrt(self, x: int) -> int:
        answer = 0
        while answer >= 0:
            if x >= answer*answer and x < (answer+1)*(answer+1):
                return answer
            answer += 1
            
# 모범 답안: binary search 사용
class Solution:
    def mySqrt(self, x: int) -> int:
        # 답은 0부터 x사이에 존재
        # 이진탐색
        # mid*mid 보다 크고 mid+1 * mid+1보다 작으면, mid가 답
        if x<=1:
            return x
        s = 0
        l = x
        while s<l:
            mid = (s+l)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid*mid:
                l = mid
            else:
                s = mid+1
        return mid+1
