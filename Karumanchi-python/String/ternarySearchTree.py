class TSTNode:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
        self.eq = None

    def _search(node,x):
        while node:
            if node.data == x:
                return node
            elif node.data > x:
                node = node.left
            else:
                node = node.right
        return None

    def _insert(node,x):
        if not node:
            return TSTNode(x)
        if x < node.data:
            node.left = TSTNode._insert(node.left,x)
        elif x > node.data:
            node.right = TSTNode._insert(node.right,x)

        return node

    # find the minimum value
    def _searchMin(node):
        while node.left:
            node = node.left
        return node

    def _deleteMin(node):
        if node.left:   
            node.left = TSTNode._deleteMin(node.left)

        return node

    def _delete(node,x):
        if node:
            if x == node.data:
                if not node.left and not node.right:
                    return None
                elif node.left and not node.right:
                    return node.left
                elif not node.left and node.right:
                    return node.right
                else:
                    tmp = TSTNode._searchMin(node.right)
                    node.data = tmp.data
                    node.right = TSTNode._delete(node.right,tmp.data)
            elif x < node.data:
                node.left = TSTNode._delete(node.left,x)
            else:
                node.right = TSTNode._delete(node.right,x)

        return node

    def _traverse(node,leaf):
        if node:
            for x in _traverse(node.left,leaf):  
                yield x
            if node.data == leaf:
                yield []
            else: 
                for x in _traverse(node.eq,leaf):
                    yield [node.data] + x
                yield [node.data]
            for x in _traverse(node.right,leaf):
                yield x

##### Ternary Search Tree #####
# 
class TST:
    def __init__(self,x=None):
        self.root = TSTNode(None)
        self.leaf = x

    def search(self,seq):
        node = self.root
        for x in seq:
            node = _search(node.eq,x)
            if not node:
                return False
        return _search(node, self.leaf) is not None

    def insert(self,seq):
        node = self.root
        for x in seq:
            child = _search(node.eq,x)
            if not child:
                child = TSTNode(x)
                node.eq = _insert(node.eq,child)
            node = child
        if not _search(node.eq,self.leaf):
            node.eq = _insert(node.eq,TSTNode(self.leaf))

        return self

    def delete(self,seq):
        node = self.root
        for x in seq:
            node = _search(node.eq,x)
            if not node:
                return self
            if not _search(node.eq,self.leaf):
                return self

        _delete(node.eq,self.leaf)

        return self

    def traverse(self):
        return _traverse(self.root.eq,self.leaf)

    def commonPrefix(self,seq):
        node = self.root
        buff = []
        for x in seq:
            buff.append(x)
            node = _search(node.eq,x)
            if not node:    
                return buff
        for x in _traverse(node.eq,self.leaf):
            yield buff + x

if __name__ == 'main':
    t = TST()
    t.insert('hello')
    t.insert('he')
    t.insert('hell')
    t.insert('helloo')

    for x in t.traverse():
        print(x)

    for x in t.commonPrefix('hell'):
        print(x)

    t.delete('hello')

    for x in t.traverse():
        print(x)
# Suffix Tree                              
                                      