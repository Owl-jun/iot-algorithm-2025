# da01_linked_list.py
# 단순 연결 리스트

# class LinkedList:
#     nodes = []
#     count = 0

#     def __init__(self,data):
#         self.__data = data
#         self.link = None
#         LinkedList.nodes.append(self)

#         self.index = LinkedList.count
#         if self.index != 0 :
#             LinkedList.nodes[self.index-1].link = self
#         LinkedList.count += 1

#     def __str__(self):
#         return f'{self.index}:{self.__data}'
    
#     @classmethod
#     def printAllList(cls):
#         for node in LinkedList.nodes:
#             print(node)

""" 위와 같이 구현하게 되면, 연결리스트가 더 필요할 때 생성할 수 없다는 것을 ! 알았습니다. """


class LinkedList:
    def __init__(self):
        self.head = None  
        self.nodes = []     

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None 
            self.next = None  

        def __str__(self):
            return f"{self.data}"

    def push_back(self, data):
        new_node = self.Node(data)  
        if not self.head:
            self.head = new_node  
            prevNode = None
        else:
            self.nodes[-1].next = new_node  
            prevNode = self.nodes[-1]
        self.nodes.append(new_node)  
        self.nodes[-1].prev = prevNode
    
    def insert(self,find_data,insert_data):
        new_node = self.Node(insert_data)
        isFind = False
        for node in self.nodes:
            if node.data == find_data:
                curNode = node
                isFind = True
                break
        if isFind == False: return    

        if curNode.prev != None:
            new_node.prev = curNode.prev
            curNode.prev.next = new_node
            curNode.prev = new_node
            new_node.next = curNode
        else : 
            self.head = new_node
            new_node.prev = None
            new_node.next = curNode
            curNode.prev = new_node

    def delete(self,del_data):
        for node in self.nodes:
            if node.data == del_data:
                delData = node
                break
        if self.head == delData:
            self.head = delData.next
        elif delData.next == None:
            delData.prev.next = None
        else:
            delData.prev.next = delData.next
            delData.next.prev = delData.prev
        del(delData)

    def find(self,find_data):
        findNode = None
        for node in self.nodes:
            if node.data == find_data:
                findNode = node
                break
        return findNode 
        
    def print_list(self):
        current = self.head
        while current:
            print(current, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":    
    list1 = LinkedList()
    list1.push_back('김씨')
    list1.push_back('왕씨')
    list1.push_back('철씨')
    list1.insert('왕씨','옹씨')
    list1.insert('씨','옹씨')
    list1.delete('철씨')
    list2 = LinkedList()
    list2.push_back('굼씨')
    list2.push_back('진씨')
    list2.insert('굼씨','주씨')
    print("List 1:")
    list1.print_list()  # 김씨 -> 왕씨 -> 철씨 -> None
    print(list1.find('김'))
    print(list1.find('김씨'))

    print("List 2:")
    list2.print_list()  # 굼씨 -> 진씨 -> None

    """ 각 인스턴스 전용 멤바변수를 설정해줌으로서 해결 """
