        if not root:
            return
        #let's do non recursive!
        count = 0   #we also count how many times we have seen finish line
        curr = root #and we use curr to traverse
        while true: #we garantee starting point not none
            
            if curr == root:  #now we decide: first time? nothing. second time? yes. Third time? we done
                count+=1
                if count == 1:
                    while curr.left:
                        curr = curr.left    #go all the way to left most                
                if count == 2:  #second time seeing it
                    curr = curr.right
                elif count == 3:
                    break   #third time, we done
    
            while curr.left:
                curr = curr.left    #garantee we are at left most

            yield curr

            if curr.right:
                curr = curr.right
            else:   #no left, no right, we at leaf
                if curr.parent and curr == curr.parent.left:    #I am a left child
                    curr = curr.parent
                else:
                    while curr.parent and curr ==curr.parent.right:
                        curr = curr.parent
                    curr = curr.parent