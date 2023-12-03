I believe Max has explained why we are trying to solve this problem, and why it is a challenge
Here I do my best to explain the design thinking behind Max's approach
For best explanations, we recommend you visit us in person at NYU Tandon Peer Tutoring Center.

Max's Traversal can be roughly broken down into three parts:
    1. How to terminate the function? (How to end the loop?)
    2. How to travel down the tree, from any given node, to the leaves?
    3. How to travel back up from a leaf to its parent, and furthur eventually to the root node?

And before we dig into these three questions, which we must answer for any kind of tree traversal 
algorithm, we must first make a few "design decisions". These decisions are entirely optional, 
and they serve to make the code shorter, more readable, and more flexible
(which is to say we can develop different traversals by recycling a large part of the algorithm)

Here is the overarching decision made by Max:

    --We only have one "yield" statement in the code

    --We only retain information of the current node that is being yielded.

And the above decision necessarily leads to the following rules:
    1. We have to use an overall "while" loop. 
      "for" loop is out of question because 
       we do not have knowledge of when to end
       the loop.
    2. As we traverse the tree, in each iteration
       of the overarching "while" loop we must 
       land on each node once and only once 
       within the subtree passed into our algorithm.
       This is because we only use one "yield"
       statement, and one node is yielded with each
       iteration of the overarching "while" loop.
       We must cover all nodes with no repetition.

So far, we both agree the above design decisions produce the most elegant code, however,
flexibility and readability is not great: It is difficult to convert Max's original design
which is an in-order traversal to a post or pre order traversal, and it is dificult to 
understand each of the three parts as described above.

Thus I propose a slight variation of Max Traversal, which is far less elegant but affords
great readability and flexibility. 

Under the folder "comprehensive breakdown", in "preorder.py", you will find a preorder
version of Max Traversal, which has the below design decisions:

    --We have two "yield" statements, but they will never both 
    be called in any iteration of the overarching "while" loop:
    One yield statement is only called when we reach the root node.
    The other only called when we reach a non-root node

    --In addition to the information of a current node being yielded,
    we also retain information of which node the root node is.

Below is "preorder.py" broken down into the three parts:

    Part1. Determining when to terminate the "while" loop:

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

In a preorder Traversal, if we follow Morries' Traversal "threading" or the textbook
"Euler Tour" method, (I will make future documentations for these two concepts)
We yield the root node the first time we pass it, we ignore the second time, and 
we finish our "threading" or "tour" the third time we pass it, which is the break
condition

    Part2. Traveling Down The Tree:

                            if node.left:
                            node = node.left
                        else:
                            if node.right:
                                node = node.right

This is the easy part of the algorithm. It is also easily converted to inorder or post order.

    Part3. Travel Back Up The Tree:

                            else:   #for sure we have leaf
                            while node != finish:
                                if node == node.parent.left:
                                    node = node.parent
                                    if node.right:
                                        node = node.right
                                        break
                                else:   #leaf is a right child
                                    node = node.parent

By the point we finish Part2, we can safetly assume any node that falls into the "else"
condition at the top of Part3 code is a leaf node with no children. Now we must use a 
property of binary tree/ binary tree node that is seldomly used: each node has information
about its own identity as a left child or right child of its parent:

                                    node == node.parent.left

The above boolen expression only evaluates to "True" when "node" variable is the left 
child of its parent, and only "False" when it is the right child. In preorder traversal,
after yeilding this leaf node, we will travel back up by one node and yield the parent in
the next iteration if the parent is one the current node's right, equivalent to saying that
the current node is the left child of its parent node; otherwise, the child must be a right
child. We ignore the parent node and travel further up, and nonstop until we reach a parent 
on the right. Thus we have a second "while" loop nested in the overarching "while" loop from
Part 1. The small catch in Part3 is, since our design decision makes it such that we cannot
finish an iteration of the overarching "while" loop and land on a node previously yielded (
because then we would have a repeatedly yielded node), when we reach any parent node that has
a right child, we immediately jump to the right child, with one exception that is when we reach
the overall root node, by which point we know we should terminate the program, which is already
handled by Part1.

This exact design thinking can be applied to post order traversal too. I might update that in the future.



