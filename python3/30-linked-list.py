

    def insert(self,head,data): 
    #Complete this method
        if head is None:
            return Node(data)
        elif head.next is None:
            head.next=Node(data)
        else:
            Solution.insert(self,head.next,data)
        return head

