import tree

class HeapNode(): # binary (degree = 2)
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Heap(Tree):
        
if __name__ == "__main__":
    import random
    Data = [random.randint(1,1000) for _ in range(1,11)]
    def Tree_Test():
        print("원래 데이터: ")
        print(Data, end="\n")
        print("힙 테스트 시작 ")
        heap = Heap()
        print("힙에 모든 요소 추가함")
        for i in range(0, len(Data)):
            heap.nodeAdd(Data[i]) # 노드에 하나씩 추가
        print("힙 추가 후: ")
        print("preorder(선위 순회): ")
        heap.preorder(heap.root) # root부터 순회
        print()
        print("inorder(중위 순회): ")
        heap.inorder(heap.root, verbose=True)
        print()
        print("postorder(후위 순회): ")
        heap.postorder(heap.root)
        print()
        print("힙 전체 구조: ")
        heap.printAll()
        print("노드 값 찾기 (마지막 값):" + str(Data[-1]))
        tree.nodeSearch(Data[-1])
        print("노드 값 찾기 (없는 값):" + str(1010))
        tree.nodeSearch(101)
        print()
        print("트리의 높이: " + str(tree.height))
        print("왼쪽 서브트리의 높이 : " + str(tree.treeHeight(lefttree.root)))
        print("오른쪽 서브트리의 높이 : " + str(tree.treeHeight(righttree.root)))
        print()
        print("왼쪽 서브트리의 노드 개수 : " + str(lefttree.size))
        print("오른쪽 서브트리의 노드 개수 : " + str(righttree.size))
        print()
        print("트리에서 노드 지우기 (5번째 값): " + str(Data[5]))
        tree.nodeDelete(Data[5])
        print("삭제하고 트리 구조: ")
        tree.printAll()
        print("트리에서 노드 지우기 (1번째 값): " + str(Data[1]))
        tree.nodeDelete(Data[1])
        print("삭제하고 트리 구조: ")
        tree.printAll()
        print("트리에서 노드 지우기 (없는 값): " + str(1090))
        tree.nodeDelete(1090)
        print("트리에서 노드 지우기 (루트 값): " + str(Data[0]))
        tree.nodeDelete(Data[0])
        print("삭제하고 트리 구조: ")
        tree.printAll()
        print("AVL트리 테스트: ")
        while True:
            if(tree.isSkewed(tree.root)):
                tree.AvlTree(tree.root)
            else:
                break
        print("현재 트리 구조: ")
        tree.printAll()
        print("트리 테스트 이상 무")
    Tree_Test()
    print("----------------------------------------")
