from queue import Queue


class TreeNode(object):

    __slots__ = 'parent', 'children', 'data'

    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0

    def add_child(self, x):
        x.parent = self
        self.children.append(x)


class Tree(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def depth(self, x):
        if x.is_root():
            return 0
        else:
            return 1 + self.depth(x.parent)

    def _height(self, x):
        if x.is_leaf():
            return 0
        else:
            return 1 + max(self._height(c) for c in x.children)

    def height(self):
        return self._height(self.root)

    def preorder(self, x):
        if not self.is_empty():
            print(x.data)
            for c in x.children:
                self.preorder(c)

    def postorder(self, x):
        if not self.is_empty():
            for c in x.children:
                self.postorder(c)
            print(x.data)

    def breadth_first(self):
        to_visit = Queue()
        to_visit.enqueue(self.root)
        while not to_visit.is_empty():
            e = to_visit.dequeue()
            print(e.data)

            for c in e.children:
                to_visit.enqueue(c)


if __name__ == '__main__':
    t = Tree()
    t.root = TreeNode(0)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.add_child(b)
    t.root.add_child(a)
    t.root.add_child(c)

    # visina stabla
    print('Visina = %d' % t.height())

    # dubina čvora
    print('Dubina(a) = %d' % t.depth(a))

    # obilazak po dubini - preorder
    print('PREORDER')
    t.preorder(t.root)

    # obilazak po dubini - postorder
    print('POSTORDER')
    t.postorder(t.root)

    # obilazak po širini
    print('BREADTH FIRST')
    t.breadth_first()
