# 링크: https://leetcode.com/problems/merge-sorted-array/
# 문제 설명: 두 오름차순 정렬된 리스트를 합하여 정렬된 하나의 리스트를 반환(여기서 새로운 메모리 할당은 금지)

# 내 풀이: list1의 길이가 m+n임을 활용하여 list1의 뒷부분에 list2를 합치고 .sort() 함수 사용
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m : m+n] = nums2
        return nums1.sort()

# 다른 풀이: 두 리스트를 뒤에서부터 비교하여, list1의 뒤에서부터 채워넣음
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while n > 0:
        if nums1[m-1] >= nums2[n-1] and m>0:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
