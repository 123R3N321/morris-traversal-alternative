from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    exp_lst = prefix_exp_str.split(" ")

    def grow_tree(exp_lst, size, node):
        if size == len(exp_lst):
            return
        else:
            item = exp_lst[size]
            size += 1
            if item.isnumeric():
                leaf = LinkedBinaryTree.Node(int(item))
                leaf.parent = node
                return leaf, size, node
            else:
                left_data = grow_tree(exp_lst, size, node)
                right_data = grow_tree(exp_lst, left_data[1], left_data[2])
                node = LinkedBinaryTree.Node(item, left_data[0], right_data[0])
                return node, right_data[1], node

    result = grow_tree(exp_lst, 0, None)[0]
    return LinkedBinaryTree(result)