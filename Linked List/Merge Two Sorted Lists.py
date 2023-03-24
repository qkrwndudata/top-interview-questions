# 링크: https://leetcode.com/problems/merge-two-sorted-lists/
# 문제 설명: 두 개의 연결리스트가 input으로 주어지면 이 두 리스트를 합해 하나의 오름차순 정렬된 연결리스트를 반환

# 풀이 1: while 문을 사용해 두 리스트의 원소를 비교해가며 새로운 연결 리스트 반환
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # merge한 결과를 저장할 연결리스트 생성
        dummy = ListNode()   # 첫 노드의 값 들어 있음
        answer = dummy   # 첫 노드를 가리키고 있음

        # 각 원소의 크기 비교
        while list1 and list2:   # list1과 list2의 원소간 크기 비교 
            if list1.val <= list2.val:
                answer.next = list1
                list1 = list1.next
            else:
                answer.next = list2
                list2 = list2.next
            answer = answer.next

            # 남은 노드 처리
            if list1 is None:
                answer.next = list2
            if list2 is None:
                answer.next = list1
        return dummy.next
    
    # 풀이 2: 새로운 연결리스트를 생성하지 않고 기존 list1을 수정해가며 재귀 알고리즘으로 구현
    class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
