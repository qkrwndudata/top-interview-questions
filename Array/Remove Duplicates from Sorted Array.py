# 링크: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 문제 설명: 오름차순(non-decreasing order)으로 중복이 허용된 리스트 nums가 주어지면 원소의 중복을 제거해 최종적으로 생성된 리스트의 길이 k를 반환
# 힌트:
## 1. 정렬된 리스트: 리스트 내 임의의 원소의 위치를 안다면 중복 여부를 확인할 수 있지 않을까?
## 2. two-pointer approach(원래 리스트 내 현재 원소의 위치 / 중복되지 않은 원소의 위치)
## 3. 임의의 원소를 마주치면 다음 중복되지 않은 원소까지 pass

### 내 풀이 
class Solution:
    def removeDuplicates(self, nums):
        curr = 1   # pointer 1: 현재 원소의 위치(1부터 시작)
        for i in range(len(nums)-1):   # pointer 2: 중복되지 않은 원소의 위치
            if nums[i+1] != nums[i]:   # 중복되지 않으면
                nums[curr] = nums[i+1]   # 현재 원소의 위치에 중복되지 않은 원소로 update 
                curr += 1
        return curr
