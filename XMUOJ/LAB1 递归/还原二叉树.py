"""1.1. 还原二叉树

输入: 二叉树的后序遍历(左右中)和中序遍历(左中右)
输出: 二叉树的层先遍历

输入样例:
7
2 3 1 5 7 6 4
1 2 3 4 5 6 7

输出样例:
4 1 6 3 5 7 2
"""

# 思路: 先递归构建二叉树, 然后层先遍历输出结果
def solve(size, postorder, inorder):
    class TreeNode:
        def __init__(self, val=0):
            self.val = val
            self.left = None
            self.right = None

    def build_tree(postorder, inorder):
        if not postorder or not inorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val) if root_val in inorder else None
        if root_index is None: return None

        root.left = build_tree(postorder[:root_index], inorder[:root_index])
        root.right = build_tree(postorder[root_index:-1], inorder[root_index + 1:])

        return root

    # 层先遍历
    def level_order_traversal(root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result
    
    # 构建二叉树
    root = build_tree(postorder, inorder)
    # 层先遍历
    result = level_order_traversal(root)
    # 输出结果
    return " ".join(map(str, result))


if __name__ == "__main__":
    n = int(input())
    postorder = list(map(int, input().split()))
    inorder   = list(map(int, input().split()))
    # 执行算法
    result = solve(n, postorder, inorder)
    # 输出结果
    print(result)