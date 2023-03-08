링크: https://leetcode.com/problems/two-sum/

### 내 풀이 ###
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# -> 문제 조건을 미루어 봤을 때 O(n^2)도 accept 되므로 가장 구현하기 쉬운 이중 for문으로 accept

### 더 나은 풀이: enumerate를 사용해 이중 for문을 피하는 방법 ###

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            temp = target - v
            if temp in nums[i+1:]:
                return [i, nums[i+1:].index(temp) + (i+1)]
                    
                
                
## 해시 테이블 사용
