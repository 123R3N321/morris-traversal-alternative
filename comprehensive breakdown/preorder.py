from LinkedBinaryTree import LinkedBinaryTree


def preorder(node):
    finish = node;
    count = 0;
    while True:
        #preorderChckYield()
        if (node == finish):
            if (count == 0):  # first time seeing it, yield it
                count += 1
                yield node
            elif (count == 1):
                break

        else:  # as long as it is not root node, we yield it
            yield node


        if node.left:
            node = node.left
        else:
            if node.right:
                node = node.right
            else:   #for sure we have leaf
                while node != finish:
                    if node == node.parent.left:
                        node = node.parent
                        if node.right:
                            node = node.right
                            break
                    else:   #leaf is a right child
                        node = node.parent