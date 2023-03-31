# 링크: https://leetcode.com/problems/binary-tree-inorder-traversal/
# 문제 설명: 주어진 binary tree에 대해 inorder traversal로 탐색한 노드의 value를 리스트로 반환

# 내 풀이: recursion을 사용하여 inorder traversal 구현
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root:
            if root.left:
                answer += self.inorderTraversal(root.left)
            answer.append(root.val)
            if root.right:
                answer += self.inorderTraversal(root.right)
            return answer
        else:
            return answer
        
# 다른 풀이: stack을 사용하여 inorder traversal 구현
def inorderTraversal(self, root):
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        if node:
            stack.append(node.right)
            stack.append(node)
            stack.append(node.left)
        else:
            if stack:
                node = stack.pop()
                res.append(node.val)
    return res
