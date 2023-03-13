# 링크: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 문제 설명: 오름차순(non-decreasing order)으로 중복이 허용된 리스트 nums가 주어지면 원소의 중복을 제거해 최종적으로 생성된 리스트의 길이 k를 반환
# 주의할 점: 또 다른 array를 위해 새로운 메모리 공간 사용 x -> set() 사용 불가
# 힌트:
## 1. 정렬된 리스트: 리스트 내 임의의 원소의 위치를 안다면 중복 여부를 확인할 수 있지 않을까?
## 2. two-pointer approach: 중복되지 않은 원소를 만나면 차례로 리스트의 앞부터 채워나감
## 3. 임의의 원소를 마주치면 다음 중복되지 않은 원소까지 pass

### 풀이 1: two pointer 사용 (while 문)
class Solution:
    def removeDuplicates(self, nums):
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] != nums[left]:   # 중복 원소가 아니면
                left += 1   # left 한 칸 이동
                nums[left] = nums[right]   # 해당 칸에 중복 아닌 원소로 update
            right += 1   # 중복 원소면 right 한 칸 이동
        return left + 1
    
### 풀이 2: two pointer 사용 (for 문)
class Solution:
    def removeDuplicates(self, nums):
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x +=1
        return(x)
    
#### 투 포인터 알고리즘: https://benn.tistory.com/9
##### 1. 1차원 배열에서 두 개의 포인터를 조작하여 원하는 결과를 얻는 알고리즘
##### 2. O(n^2)을 O(n)으로 풀 수 있음
##### 3. start(left)-end(right) / slow-fast
