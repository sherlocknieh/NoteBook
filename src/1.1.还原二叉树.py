# 1.1. 还原二叉树

# 输入: 二叉树的后序遍历(左右中)和中序遍历(左中右)
# 输出: 二叉树的层先遍历
# 条件: 二叉树中没有重复的元素

# 输入样例:
# 7
# 2 3 1 5 7 6 4
# 1 2 3 4 5 6 7

# 输出样例:
# 4 1 6 3 5 7 2

# 思路1: 先递归构建二叉树, 然后层先遍历输出结果
def algorithm1(size: int, postorder: list[int], inorder: list[int]):
    class TreeNode:
        def __init__(self, val=0):
            self.val: int = val
            self.left: TreeNode | None = None
            self.right: TreeNode | None = None

    def build_tree(postorder: list[int], inorder: list[int]) -> TreeNode | None:
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
    def level_order_traversal(root: TreeNode | None) -> list[int]:
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

# 思路2: 把后序遍历和中序遍历当作特殊形态的二叉树用, 直接进行层先遍历
def algorithm2(size, postorder, inorder):
    if size <= 0:
        print("")
        return

    # 用哈希表定位根节点在中序中的位置，避免重复线性查找
    in_index = {}
    i = 0
    while i < size:
        in_index[inorder[i]] = i
        i += 1

    result = []
    # 队列元素: (in_l, in_r, post_l, post_r)
    import collections
    queue = collections.deque()
    queue.append((0, size - 1, 0, size - 1))

    while queue:
        in_l, in_r, post_l, post_r = queue.popleft()
        if in_l > in_r:
            continue

        root = postorder[post_r]
        result.append(root)

        root_pos = in_index[root]
        left_size = root_pos - in_l
        right_size = in_r - root_pos

        # 先入左子树再入右子树，保证层序从左到右
        if left_size > 0:
            queue.append((in_l, root_pos - 1, post_l, post_l + left_size - 1))
        if right_size > 0:
            queue.append((root_pos + 1, in_r, post_l + left_size, post_r - 1))

    return " ".join(map(str, result))

def main():
    # 输入处理
    n = int(input())
    postorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    # 执行算法
    result = algorithm1(n, postorder, inorder)
    # 输出结果
    print(result)

def test():
    n = 7
    postorder = [2, 3, 1, 5, 7, 6, 4]
    inorder = [1, 2, 3, 4, 5, 6, 7]
    # 计时
    import time
    t0 = time.time()
    result1 = algorithm1(n, postorder, inorder)
    t1 = time.time()
    result2 = algorithm2(n, postorder, inorder)
    t2 = time.time()

    print(f"algorithm1 execution time: {t1 - t0}")
    print(f"algorithm2 execution time: {t2 - t1}")
    print(f"algorithm1 result: {result1}")
    print(f"algorithm2 result: {result2}")
    
    assert result1 == "4 1 6 3 5 7 2"
    assert result2 == "4 1 6 3 5 7 2"
    print("🟢 test passed")

def temp():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = list1[:-1]
    print(list2)

if __name__ == "__main__":
    #temp()
    test()
    #main()