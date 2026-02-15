# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # find distance upstream and downstream

        # downstream easy, just have a flag indicating target is found and track dist

        # start by finding target
        # once target is found we can identify the ones downstream
        # could track parents of each node and then find upstream
        # so basically do bfs and keep a list of seen nodes
        # could also make an adj list and do dfs / bfs in one pass

        parents = dict()

        def helper(node, parent):
            if node is None:
                return

            parents[node] = parent

            if node == target:
                return
            
            helper(node.right, node)
            helper(node.left, node)

        helper(root, None)

        res = set()
        seen = set()

        def find_downstream(node, dist):
            if node is None:
                return
            
            seen.add(node.val)

            if dist == 0:
                res.add(node.val)
                return
            
            find_downstream(node.right, dist - 1)
            find_downstream(node.left, dist - 1)

        find_downstream(target, k)

        def find_upstream(node, dist):
            if node is None or node.val in seen:
                return 

            seen.add(node.val)
            if dist == 0:
                res.add(node.val)
                return
            
            find_upstream(parents[node], dist - 1)
            find_upstream(node.right, dist - 1)
            find_upstream(node.left, dist - 1)

        seen.remove(target.val)
        find_upstream(target, k)

        return list(res)

            
            

            

        












        
