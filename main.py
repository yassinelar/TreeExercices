import copy
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def display(root):
    if root == None:
        return None
    else:
        print(root.data, end = ' ')
        display(root.left)
        display(root.right)

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

def switch(root):
    t = root.left
    root.left = root.right
    root.right = t

def mirror(root):
    if (root == None):
        return None
    else:
        mirror(root.left)
        mirror(root.right)
        switch(root)

def symmetrical(root1, root2):
    if (root1 == None and root2 == None):
        return True
    elif (root1 == None or root2 == None):
        return False
    else:
        return (root1.data == root2.data and symmetrical(root1.left, root2.right) and symmetrical(root1.right, root2.left))

def isSymmetrical(root):
    return symmetrical(root, root)

def isBalanced(root):
    if (not root):
        return 1
    else:
        result = height(root.right) - height(root.left)
        return (abs(result) <= 1 and isBalanced(root.left) and isBalanced(root.right))


def isSumProperty(root):
    # code here
    if root == None or root.left == None and root.right == None:
        return 1
    elif (root.left == None and root.right):
        if (root.right.data == root.data) :
            condition = 1
        else:
            condition = 0
        return (condition and isSumProperty(root.right))
    elif (root.right == None and root.left):
        if (root.left.data == root.data) :
            condition = 1
        else:
            condition = 0
        return (condition and isSumProperty(root.left))
    else:
        if (root.left.data + root.right.data == root.data):
            condition = 1
        else:
            condition = 0
        return (condition and isSumProperty(root.left) and isSumProperty(root.right))


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
    print("Height: ", height(root))

    # Identical trees
    root1 = copy.deepcopy(root)
    root2 = copy.deepcopy(root)
    root1.right.right = Node(6)
    print("isIdentical: ", isIdentical(root1, root2))

    #Mirror tree
    print("Mirror: ")
    root_M = copy.deepcopy(root)
    mirror(root_M)
    display(root_M)

    #Symmetrical trees
    ''' Construct the following tree
                  1
                /   \
               /     \
              3       3
             / \     / \
            2   8   8   2   
        '''

    root_sym = Node(1)
    root_sym.left = Node(3)
    root_sym.right = Node(3)
    root_sym.left.left = Node(2)
    root_sym.left.right = Node(8)
    root_sym.right.left = Node(8)
    root_sym.right.right = Node(2)
    print("\n" + "isSymmetrical: ")
    print(isSymmetrical(root_sym))

    #Balanced Tree
    root_balanced = copy.deepcopy(root)
    print("Balanced tree: " + "\n" + "L: ", height(root.left), "R: ", height(root.right))
    print(isBalanced(root))

    #Children Sum parent
    root_sum = copy.deepcopy(root)
    print("isSumProperty")
    print(isSumProperty(root))  #false
    ''' Construct the following tree
                      6
                    /   \
                   /     \
                  3       3
                 / \     / \
                2   1   0   3  
            '''

    root_sum = Node(6)
    root_sum.left = Node(3)
    root_sum.right = Node(3)
    root_sum.left.left = Node(2)
    root_sum.left.right = Node(1)
    root_sum.right.left = Node(0)
    root_sum.right.right = Node(3)
    print(isSumProperty(root_sum))  #True
