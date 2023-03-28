# 링크: https://leetcode.com/problems/climbing-stairs/
# 문제 설명: n 높이의 계단이 있을 때 한 번에 1층 또는 2층씩 오를 수 있다면, 정상에 도달할 경우의 수를 구하는 문제

# 내 풀이: fibonacci 수열
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            a, b = 1, 2
            for i in range(n-2):
                a, b = b, a+b
        return b
    
# 다른 풀이: Dynamic programming
def climb(n):
    #edge cases
    if n==0: return 0
    if n==1: return 1
    if n==2: return 2
    dp = [0]*(n+1) # considering zero steps we need n+1 places
    dp[1]= 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] +dp[i-2]
    print(dp)
    return dp[n]
		
# 알고리즘 설명: [다이나믹 프로그래밍](참고: https://hongjw1938.tistory.com/47)
