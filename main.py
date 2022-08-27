# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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

    print (height(root))
