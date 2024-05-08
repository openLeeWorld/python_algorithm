class TreeNode(): # binary (degree = 2)
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree(): #BinarySearchTree
    def __init__(self):
        self.root = None
        self.parent = None
        self.child = None
        self.height = None
        self.size = 0
    
    def LeftSubTree(self, node):
        # 왼쪽 서브트리 생성
        if(node == None):
            #print("트리가 없습니다.")
            return None
        
        else:
            leftTree = Tree()
            leftTree.root = node.left
            leftTree.height = self.treeHeight(leftTree.root)
            leftTree.size = self.inorder(leftTree.root, verbose=False) # 중위 순회로 노드 개수를 셈
        
        return leftTree
    
    def RightSubTree(self, node):
        # 오른쪽 서브트리 생성
        if(node == None):
            #print("트리가 없습니다.")
            return None
        
        else:
            rightTree = Tree()
            rightTree.root = node.right
            rightTree.height = self.treeHeight(rightTree.root)
            rightTree.size = self.inorder(rightTree.root, verbose=False)
        
        return rightTree
        
    def treeHeight(self, node):
        if(node == None):
            return 0
        
        else:
            if(node.left == None and node.right == None):
                return 0
            
            elif(node.left != None and node.right == None):
                return self.treeHeight(node.left) + 1

            elif(node.left == None and node.right != None):
                return self.treeHeight(node.right) + 1
            
            elif(node.left != None and node.right != None):
                return max(self.treeHeight(node.left), self.treeHeight(node.right)) + 1
            
    def isSkewed(self, node):
        leftTree = self.LeftSubTree(node)
        rightTree = self.RightSubTree(node)
        
        if(abs(leftTree.height - rightTree.height) >= 2):
            return True
        
        else:
            return False
        
    def AvlTree(self, node): # 삭제하느라 skewed된 트리를 밸런스를 수정함(높이가 1 높은 트리를 낮은 트리로 노드를 옮김) 
        #node를 기준으로 서브트리를 avl 트리 변환을 수행함
        
        def maxLeftSubTreeValue(leftTree): 
            node = leftTree.root # 왼쪽 서브트리의 루트 노드
            if(node == None):
                return None
            
            else:
                while(node.right != None):
                    node = node.right
                
            maxValue = node.data
            return maxValue
        
        def minRightSubTreeValue(rightTree): 
            node = rightTree.root # 오른쪽 서브트리의 루트 노드
            if(node == None):
                return None
            
            else:
                while(node.left != None):
                    node = node.left
                
            minValue = node.data
            return minValue
        
        leftTree = self.LeftSubTree(node)
        rightTree = self.RightSubTree(node)
        
        if(self.isSkewed(node)): # skewd tree일 때
            if(leftTree.height > rightTree.height): # 왼쪽이 더 큰 서브트리
                RootValue = node.data
                replaceValue = maxLeftSubTreeValue(leftTree)
                self.nodeDelete(replaceValue)
                node.data = replaceValue
                self.nodeAdd(RootValue)
                
                    
            elif(leftTree.height < rightTree.height): # 오른쪽이 더 큰 서브트리
                RootValue = node.data
                replaceValue = minRightSubTreeValue(rightTree)
                self.nodeDelete(replaceValue)
                node.data = replaceValue
                self.nodeAdd(RootValue)
                
            print("avl트리 연산 1회 완료")
            return
    
        else:
            print("avl트리상태입니다.")
            return
        
    def printAll(self):
        if(self.root == None):
            print("트리가 비었습니다.")
            return
        else:
            self.printNode(self.root, 0) # 루트부터 전부 출력, 각 left, right 깊이 = 0
            print()
            
    def printNode(self, node, count): # 해당 노드를 루트로 하는 서브트리 출력, count는 출력 상대 위치
        if(node == None):
            #print("해당 루트가 없습니다.")
            return
        else:
            data = node.data
            print("--%d" % data, end="\n")
            string_format = ""
            depth = count + 1 # 자식 노드 출력 깊이
            
            if(node.left == None and node.right == None):
                return
            
            elif(node.left != None and node.right == None):
                left = node.left
                for _ in range(depth): # 왼쪽 노드의 프린트 위치 계산
                    string_format += "   " # 3칸
                print(string_format, end="")
                print("|", end="")
                
                self.printNode(left, depth)
                return
                
            elif(node.left == None and node.right != None):
                right = node.right
                for _ in range(depth): # 오른쪽 노드의 프린트 위치 계산
                    string_format += "   " # 3칸
                print(string_format, end="")
                print("|", end="")

                self.printNode(right, depth)
                return
            
            else: # 두 자식 있을 때
                left = node.left
                right = node.right
                for _ in range(depth): # 왼쪽 노드의 프린트 위치 계산
                    string_format += "   " # 3칸
                print(string_format, end="")
                print("|", end="")

                self.printNode(left, depth)
                
                print(string_format, end="")
                print("|", end="")
                self.printNode(right, depth)
                
                return
            
    def preorder(self, node): # node : 시작점
        if(node == None):
            return
        
        print(node.data, end='->')
        self.preorder(node.left)
        self.preorder(node.right)
        
    def inorder(self, node, verbose=True): # verbose=False는 self.size세는 용도
        if(verbose == True):
            if(node == None):
                return 
            
            else:
                self.inorder(node.left, verbose=True)
                print(node.data, end='->')
                self.inorder(node.right, verbose=True)
                return
        
        elif(verbose == False):
            if(node == None):
                count = 0
                return count
            else:
                count_left = self.inorder(node.left, verbose=False)
                count_right = self.inorder(node.right, verbose=False)
                return count_left + count_right + 1
            
    def postorder(self, node):
        if(node == None):
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end='->')
        
    def nodeAdd(self, data):
        newNode = TreeNode(data)
        if(self.root == None): # 빈 tree일 시 초기화
            self.root = newNode
            self.parent = self.child = self.root
            self.height = 0
            self.size = self.size + 1
        else: # 노드가 1개 이상일시 leaf에 추가
            self.parent = self.root
            count = 0
            while self.parent.left != None or self.parent.right != None: # 해당 위치 까지 이동(leaf까지 이동)
                if(self.parent.data > data): # 값이 작을 경우 왼쪽으로
                    if(self.parent.left == None): # 왼쪽이 빈 경우
                        self.parent.left = newNode
                        self.child = self.parent.left
                        count = count + 1
                        break # 추가 후 나감
                    else: # 왼쪽으로 이동 가능할 경우
                        self.parent = self.parent.left
                        count = count + 1
                elif(self.parent.data < data): # 값이 클 경우 오른쪽으로
                    if(self.parent.right == None): # 오른쪽이 빈 경우
                        self.parent.right = newNode
                        self.child = self.parent.right
                        count = count + 1
                        break # 추가 후 나감
                    else: # 오른쪽으로 이동 가능할 경우
                        self.parent = self.parent.right
                        count = count + 1
                elif(self.parent.data == data): # bst에서는 값이 중복되면 안됨
                    print("중복된 값 노드가 있어 추가되지 않습니다.")
                    return
                else: # 오류케이스
                    print("올바른 데이터 값이 아닙니다")
                    raise ValueError
            # 노드가 리프에 온 경우
            if(self.parent.left == None and self.parent.right == None):
                if(self.parent.data > data): # 값이 작을 경우 왼쪽으로
                    self.parent.left = newNode
                    self.child = self.parent.left
                    count = count + 1
                elif(self.parent.data < data): # 값이 클 경우 오른쪽으로
                    self.parent.right = newNode
                    self.child = self.parent.right
                    count = count + 1
                elif(self.parent.data == data): # bst에서는 값이 중복되면 안됨
                    print("중복된 값 노드가 있어 추가되지 않습니다.")
                    return
                else: # 오류케이스
                    print("올바른 데이터 값이 아닙니다")
                    raise ValueError
                
            self.size = self.size + 1  # 트리 노드 개수 추가
            if(count > self.height): # 제일 많이 내려간 케이스면 높이 수정
                self.height = count
                
    def nodeSearch(self, data):
        if(self.root == None):
            print("트리가 비었습니다.")
            return
        else:
            node = self.root
            
            while node.left != None or node.right != None: # 해당 위치 까지 이동(leaf까지 이동)
                if(node.data > data): # 값이 작을 경우 왼쪽으로
                    if(node.left != None):
                        node = node.left
                    else:
                        print(str(data) +"값이 없습니다.")
                        return False
                    
                elif(node.data < data): # 값이 클 경우 오른쪽으로
                    if(node.right != None):
                        node = node.right
                    else:
                        print(str(data) +"값이 없습니다.")
                        return False
                    
                elif(node.data == data): # 찾음!
                    print(str(data) +  "값을 찾았습니다.")
                    return True
                
                else: # 오류케이스
                    print("올바른 데이터 값이 아닙니다")
                    raise ValueError
                
            # 노드가 리프에 온 경우
            if(node.left == None and node.right == None):
                if(node.data == data):
                    print(str(data) + "값을 찾았습니다.")
                    return True
                else:
                    print(str(data) +"값이 없습니다.")
                    return False
                
    def nodeDelete(self, data):
        
        def maxLeftSubTreeValue(leftTree): 
            node = leftTree.root # 왼쪽 서브트리의 루트 노드
            if(node == None):
                return None
            
            else:
                while(node.right != None):
                    node = node.right
                
            maxValue = node.data
            return maxValue
        
        def minRightSubTreeValue(rightTree): 
            node = rightTree.root # 오른쪽 서브트리의 루트 노드
            if(node == None):
                return None
            
            else:
                while(node.left != None):
                    node = node.left
                
            minValue = node.data
            return minValue
            
        
        if(self.nodeSearch(data) == False):
            print("삭제하려는 값이 트리에 없습니다.")
            return
        
        else: # 값 위치를 찾아 parent와 node에 넣고 조작한다.
            node = self.root
            parent = node
            
            while node.left != None or node.right != None: # 해당 위치 까지 이동
                if(node.data > data): # 값이 작을 경우 왼쪽으로
                    if(node.left != None):
                        parent = node
                        node = node.left
                        
                elif(node.data < data): # 값이 클 경우 오른쪽으로
                    if(node.right != None):
                        parent = node
                        node = node.right
                        
                elif(node.data == data): # 찾음!
                    break
                
            # 삭제 케이스를 나눠서 트리 조작   
            if(node.data == self.root.data): # 삭제하려는 값이 루트인경우 -> 왼쪽 서브트리 가장 큰 수를 루트로 하고 연결하고 원래 그 값은 삭제함.
                if(self.size == 1): # 루트 밖에 없을 시
                    self.root = None
                    del node
                    
                else:
                    leftTree = self.LeftSubTree(self.root) # 왼쪽 서브트리 생성
                    RightTree = self.RightSubTree(self.root) # 왼쪽 서브트리 생성
                    if(leftTree.root != None): # 왼쪽 서브트리가 존재할 경우
                        replaceValue = maxLeftSubTreeValue(leftTree) # 왼쪽 서브트리의 가장 큰 값을 반환
                        self.nodeDelete(replaceValue) # 루트 추가전에 미리 서브트리에서 제거함 (리프나 자식 1개 케이스임)
                        self.root.data = replaceValue
                        
                    else: # 왼쪽 서브트리가 없으므로 오른쪽 서브트리의 가장 작은 값으로 대체함
                        replaceValue = minRightSubTreeValue(RightTree) # 오른쪽 서브트리의 가장 작은 값을 반환
                        self.nodeDelete(replaceValue) # 루트 추가전에 미리 서브트리에서 제거함 (리프나 자식 1개 케이스임)
                        self.root.data = replaceValue
                    
            elif(node.left == None and node.right == None): # 삭제하려는 값이 리프인경우 -> 그냥 지움
                if(parent.left == node):
                    parent.left = None
                    
                elif(parent.right == node):
                    parent.right = None
                
                node = None
                del node    
                
            elif(node.left != None and node.right == None): # 삭제하려는 값이 자식이 왼쪽 하나인경우 
                if(parent.left == node):
                    parent.left = node.left
                    
                elif(parent.right == node):
                    parent.right = node.left
                
                node.left = None
                node = None
                del node
                
                
            elif(node.left == None and node.right != None): # 삭제하려는 값이 자식이 오른쪽 하나인경우 
                if(parent.left == node):
                    parent.left = node.right
                    
                elif(parent.right == node):
                    parent.right = node.right
                
                node.right = None
                node = None
                del node
                
            elif(node.left != None and node.right != None): # 삭제하려는 값이 자식이 둘인경우 -> 왼쪽 서브트리 최대값이나 오른쪽 서브트리 최소값으로 대체
                leftTree = self.LeftSubTree(node) # 왼쪽 서브트리 생성
                RightTree = self.RightSubTree(node) # 왼쪽 서브트리 생성
                if(leftTree.root != None): # 왼쪽 서브트리가 존재할 경우
                    replaceValue = maxLeftSubTreeValue(leftTree) # 왼쪽 서브트리의 가장 큰 값을 반환
                    self.nodeDelete(replaceValue) # 루트 추가전에 미리 서브트리에서 제거함 (리프나 자식 1개 케이스임)
                    node.data = replaceValue
                        
                else: # 왼쪽 서브트리가 없으므로 오른쪽 서브트리의 가장 작은 값으로 대체함
                    replaceValue = minRightSubTreeValue(RightTree) # 오른쪽 서브트리의 가장 작은 값을 반환
                    self.nodeDelete(replaceValue) # 루트 추가전에 미리 서브트리에서 제거함 (리프나 자식 1개 케이스임)
                    node.data = replaceValue
                
            else:
                print("구현되지 않은 삭제입니다.")
                return
            
            #finally
            self.size = self.size - 1  
            self.height = self.treeHeight(self.root)
            print("해당 값을 트리에서 삭제하였습니다.")
            return
            
if __name__ == "__main__":
    import random
    Data = [random.randint(1,1000) for _ in range(1,31)]
    def Tree_Test():
        print("원래 데이터: ")
        print(Data, end="\n")
        print("트리 테스트 시작 ")
        tree = Tree()
        print("트리에 모든 요소 추가함")
        for i in range(0, len(Data)):
            tree.nodeAdd(Data[i]) # 노드에 하나씩 추가
        print("트리 추가 후: ")
        print("preorder(선위 순회): ")
        tree.preorder(tree.root) # root부터 순회
        print()
        print("inorder(중위 순회): ")
        tree.inorder(tree.root, verbose=True)
        print()
        print("postorder(후위 순회): ")
        tree.postorder(tree.root)
        print()
        print("트리 전체 구조: ")
        tree.printAll()
        lefttree = tree.LeftSubTree(tree.root) # subtree개념을 이용하려면 반드시 호출
        righttree = tree.RightSubTree(tree.root)
        print("왼쪽 서브트리 구조: ")
        tree.printNode(lefttree.root, 0)
        print()
        print("오른쪽 서브트리 구조: ")
        tree.printNode(righttree.root, 0)
        print()
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
