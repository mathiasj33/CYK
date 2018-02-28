class CFG:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        else:
            return '{}({},{})'.format(self.data, self.left, self.right)
