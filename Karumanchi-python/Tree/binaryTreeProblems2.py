
# given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

def treeMaxSumPath(node,is_left=True,Lpath={},Rpath={}):
    if is_left:
        if not node.left:
            Lpath[node.id] = 0
            return 0
        else:
            pass