'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

'''


class TreeNode:

    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val


class Solution:

    def merge_tree(self, t1: TreeNode, t2: TreeNode):
        if not t1 or not t2:
            return t1 or t2
        t1.val = t1.val + t2.val
        t1.left = self.merge_tree(t1.left, t2.left)
        t1.right = self.merge_tree(t1.right, t2.right)
        return t1


solution = Solution()

left = TreeNode(None, None, 1)
right = TreeNode(None, None, 2)
root1 = TreeNode(left, right, 0)
root2 = TreeNode(left, right, 1)
result = solution.merge_tree(root1, root2)
print("root:", result.val, "root.left", result.left.val, "root.right", result.right.val)
