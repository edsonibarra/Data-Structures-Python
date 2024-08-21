class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        new_node.next = cur_node
        self.head = new_node

    def print_list(self):
        if self.head is None:
            return
        cur_node = self.head
        while cur_node:
            print(f"[{cur_node.data}]", end="->")
            cur_node = cur_node.next
        print("None")

    def delete_by_value(self, key):
        if self.head is None:
            return
        cur_node = self.head
        prev= None
        # Case: key matches first node data
        if cur_node.data == key:
            # Change the pointer to the next node
            self.head = cur_node.next
            # Delete the cur_node
            cur_node = None
            return
        # Case: node to delete is not the first one
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        # Node with Node.data == key was found
        if cur_node:
            prev.next = cur_node.next
            cur_node = None
            return
        # Node.data == key was not found
        return

    def delete_by_position(self, position: int) -> None:
        if self.head is None:
            return
        cur_node = self.head
        prev = None
        count = 0
        while cur_node and count != position:
            count += 1
            prev = cur_node
            cur_node = cur_node.next
        if cur_node:
            prev.next = cur_node.next
            cur_node = None
            return
        return
    
    def __len__(self) -> int:
        node_count = 0
        cur_node = self.head
        while cur_node:
            node_count += 1
            cur_node = cur_node.next
        return node_count

    def reverse(self):
        if self.head is None:
            return
        cur_node = self.head
        prev = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
        self.head = prev
    
    def remove_duplicates(self):
        """
        The key to understand this
        method is to know that it is
        deleting nodes in place, aka
        while it's iterating over
        the linked list.
        
        In difference to the delete_by_value
        and delete_by_position methods where
        the iteration stops when finds the
        node with the contitions to delete.
        """
        if self.head is None:
            return
        seen = {}
        cur_node = self.head
        prev = None
        while cur_node:
            if cur_node.data in seen.keys():
                prev.next = cur_node.next
                cur_node = None
            else:
                seen[cur_node.data] = True
                prev = cur_node
            cur_node = prev.next
            


def main():
    l = SinglyLinkedList()
    for n in range(1, 11):
        l.append(n)
    l.print_list()
    l.reverse()
    l.print_list()
    print()
    l.append(10)
    l.print_list()
    l.remove_duplicates()
    l.print_list()
    

if __name__ == "__main__":
    main()

