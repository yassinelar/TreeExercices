import copy
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def height(root):
    if (root == None) :
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

def isIdentical(root1, root2):
    if ((root1 != None and root2 != None and root1.data != root2.data) or (root1 != None and root2 == None) or (root2 != None and root1 == None)):
        return False
    elif (root1 == None and root2 == None):
        return True
    else:
        return True and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)


if __name__ == '__main__':
    ''' Construct the following tree
              1
            /   \
           /     \
          3       5
         / \     / 
        2   8   1   
    '''

    root = Node(1)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(8)
    root.right.left = Node(1)

    # Height of binary tree
    print(height(root))

    # identical trees
    root1 = copy.deepcopy(root)
    root1.right.right = Node(6)
    print(isIdentical(root, root1))
