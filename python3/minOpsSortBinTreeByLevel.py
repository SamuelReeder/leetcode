# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        levels = []

        def helper(root, level):
            if root is None:
                return

            if level >= len(levels):
                levels.append([])

            levels[level].append(root.val)

            helper(root.left, level + 1) 
            helper(root.right, level + 1)

        helper(root, 0)

        cnt = 0
        for l in range(1, len(levels)):

            tmp = sorted(levels[l])

            hm = {val: i for i, val in enumerate(tmp)}

            visited = [False] * len(levels[l])

            for i in range(len(levels[l])):
                tmp = levels[l][i]
                if visited[i] or i == hm[tmp]:
                    continue

                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = hm[levels[l][j]]
                    cycle_size += 1
                
                # If a cycle has length K, we need K-1 swaps to resolve it
                if cycle_size > 1:
                    cnt += (cycle_size - 1)
                    
        return cnt








        
