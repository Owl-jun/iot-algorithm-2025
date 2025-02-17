import da01_linked_list as l

dataArray = [["지민","010-1111-1111"],["정국","010-2222-2222"],["뷔","010-3333-3333"],["슈가","010-4444-4444"],["진","010-5555-5555"]]


makeSimpleLinkedList = l.LinkedList()
for data in dataArray:
    makeSimpleLinkedList.push_back(data)

makeSimpleLinkedList.print_list()