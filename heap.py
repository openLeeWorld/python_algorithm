class HeapNode(): # binary (degree = 2)
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.index = 0  # 노드 별 인덱스 내용(0~)
        
class Heap(): 
    def __init__(self, mode):
        self.root = None
        self.height = 0
        self.size = 0
        self.mode = mode # minHeap or maxHeap
        
    def returnRoot(self):
        if(self.root != None):
            return self.root.data
        
        else:
            print("빈 힙입니다.")
            return
        
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
            
    def printAll(self):
        if(self.root == None):
            print("힙이 비었습니다.")
            return
        else:
            self.printNode(self.root, 0) # 루트부터 전부 출력, 각 left, right 깊이 = 0
            print()
            
    def printNode(self, node, count): # 해당 노드를 루트로 하는 서브트리 출력, count는 출력 상대 위치
        if(node == None):
            
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
        
    def findNodeByIndex(self, index):
        if(index == 0):
            return self.root
        
        else:
            direction = [] # 왼쪽은 true, 오른쪽은 false
            quotient = index
            remainder = -1
            while (quotient != 0): # 루트에 오면 종료
                remainder = quotient % 2 # 홀수면 왼쪽, 짝수면 오른쪽
                
                if(remainder == 1):
                    direction.append(True)
                    
                elif(remainder == 0):
                    direction.append(False)
                
                quotient = (quotient-1) // 2
                    
            node = self.root 
            
            while(direction != []):
                mv_dir = direction.pop()
                if(mv_dir == True):
                    node = node.left
                    
                elif(mv_dir == False):
                    node = node.right   
        
        return node    
    
    def percolate(self, newNode): # 노드가 부모와 위치를 변경해감
        if(newNode != None):
            node = newNode
        else:
            return
        
        if(self.mode == "minHeap"): # 삽입 후 마지막 요소가 위의 큰 값과 교체해감
            while node.parent != None: # 자식이 더 작을 경우 swap 계속
                if(node.data < node.parent.data):       
                    temp = node.data
                    node.data = node.parent.data
                    node.parent.data = temp
        
                    node = node.parent
                    
                else:
                    break
                
        elif(self.mode == "maxHeap"): # 삽입 후 마지막 요소가 위의 작은 값과 교체해감
            while node.parent != None: # 자식이 더 클 경우 swap 계속
                if(node.data > node.parent.data):       
                    temp = node.data
                    node.data = node.parent.data
                    node.parent.data = temp
        
                    node = node.parent
                    
                else:
                    break
        #print("percolate완료!")    
        return
    
    def percolate_down(self, newNode): # 노드가 자식과 위치 변경해감
        if(newNode != None):
            node = newNode
        else:
            return
        
        if(self.mode == "minHeap"): # 삭제 후 마지막 요소가 위의 큰 값과 교체해감
            while node.left != None or node.right != None: 
                if(node.left != None and node.right!= None):  
                    if(node.data > node.left.data and node.left.data <= node.right.data): # 왼쪽 자식이 제일 작을 경우 swap 계속
                        temp = node.data
                        node.data = node.left.data
                        node.left.data = temp
            
                        node = node.left
                        
                    elif(node.data > node.right.data and node.left.data > node.right.data): #더 작은 쪽의 자식과 교체   
                        temp = node.data
                        node.data = node.right.data
                        node.right.data = temp
            
                        node = node.right
                        
                    else: # 더이상 움직이지 않으면 break
                        break
                    
                elif(node.left != None and node.right == None):
                    if(node.data > node.left.data):
                        temp = node.data
                        node.data = node.left.data
                        node.left.data = temp
            
                        node = node.left
                        
                    else: # 더이상 움직이지 않으면 break
                        break
                    
                elif(node.left == None and node.right != None):
                    if(node.data > node.right.data):
                        temp = node.data
                        node.data = node.right.data
                        node.right.data = temp
            
                        node = node.right
                        
                    else: # 더이상 움직이지 않으면 break
                        break
                        
                else: # leaf이면 끝
                    break
            
        elif(self.mode == "maxHeap"): # 삽입 후 마지막 요소가 위의 작은 값과 교체해감
            while node.left != None or node.right != None: 
                if(node.left != None and node.right!= None):  
                    if(node.data < node.left.data and node.left.data > node.right.data): # 왼쪽 자식이 제일 클 경우 swap 계속
                        temp = node.data
                        node.data = node.left.data
                        node.left.data = temp
            
                        node = node.left
                        
                    elif(node.data <= node.right.data and node.left.data <= node.right.data): #더 큰 쪽의 자식과 교체   
                        temp = node.data
                        node.data = node.right.data
                        node.right.data = temp
            
                        node = node.right
                        
                    else: # 더이상 움직이지 않으면 break
                        break
                    
                elif(node.left != None and node.right == None):
                    if(node.data <= node.left.data):
                        temp = node.data
                        node.data = node.left.data
                        node.left.data = temp
            
                        node = node.left
                        
                    else: # 더이상 움직이지 않으면 break
                        break
                    
                elif(node.left == None and node.right != None):
                    if(node.data <= node.right.data):
                        temp = node.data
                        node.data = node.right.data
                        node.right.data = temp
            
                        node = node.right
                        
                    else: # 더이상 움직이지 않으면 break
                        break
                        
                else:
                    break
                
        #print("percolate완료!")    
        return      

    def nodeAdd(self, data): # heap은 complete구조를 만들고 percolate하여 값을 맞춤
        newNode = HeapNode(data)
        
        if(self.root == None): # 빈 tree일 시 초기화
            self.root = newNode
            self.height = 0
            self.size = self.size + 1
            self.root.index = 0
            
            return
            
        else: # 노드가 1개 이상일시 구조에 맞춰 leaf에 추가 
            nextIndex = self.size 
            newNode.index = nextIndex # 노드의 인덱스 설정
            parent = self.findNodeByIndex((nextIndex-1) // 2) # 부모 노드 찾기
            newNode.parent = parent # 부모 연결   
            
            if(nextIndex % 2 == 1):
                parent.left = newNode
            elif(nextIndex % 2 == 0):
                parent.right = newNode
        
            self.percolate(newNode) # 해당 노드의 값을 올바른 위치로
            #finally 
            self.size = self.size + 1  # 힙 노드 개수 추가
            if(self.size >= 2 ** (self.height+1)):
                self.height = self.height + 1 # 높이 업데이트
                
            return 
        
    def nodeSearch(self, data):
        if(self.root == None):
            print("힙이 비었습니다.")
            return False
        
        else:
            for i in range(self.size):
                node = self.findNodeByIndex(i) # 하나하나 대조해보기
                if(node.data == data):
                    #print(str(data) + "값을 찾았습니다.")
                    return True
            
            print("값이 힙에 없습니다.")
            return False
        
    def nodeDelete(self, data):
        if(self.nodeSearch(data) == False):
            print("삭제하려는 값이 힙에 없습니다.")
            return
        
        else: # 마지막 값을 삭제하려는 값에 대입하고 자식들 중 더 큰 값으로 percolate - down 한다.
            for i in range(self.size):
                node = self.findNodeByIndex(i)
                if(node.data == data):
                    break
                
            lastIndex = self.size - 1
            lastNode = self.findNodeByIndex(lastIndex)
            deleteNode = node
            
            if(lastNode == deleteNode or lastNode.parent == None): # heap 한 개를 삭제할 경우
                self.root = None
                del lastNode
                self.size = self.size - 1
                return
            
            # swap
            temp = lastNode.data 
            lastNode.data = deleteNode.data
            deleteNode.data = temp
            #lastNode는 연결을 끊고 삭제한다.
            parent = lastNode.parent
            if(parent != None): # 루트가 아닐 경우
                if(parent.left == lastNode):
                    parent.left = None
                elif(parent.right == lastNode):
                    parent.right = None
                
                lastNode.parent = None
                del lastNode 
                
            # deleteNode는 percolate한다.  
            parent = deleteNode.parent
            if(parent != None): # 루트값이 아닐 때
                if(self.mode == "minHeap"):
                    if(parent.data > deleteNode.data): # 부모가 갈아친 노드보다 큰 경우
                        self.percolate(deleteNode)
                        
                    else: 
                        self.percolate_down(deleteNode)
                        
                elif(self.mode == "maxHeap"):
                    if(parent.data < deleteNode.data): # 부모가 갈아친 노드보다 작은 경우
                        self.percolate(deleteNode)
                        
                    else: 
                        self.percolate_down(deleteNode)
                        
            else: # 루트랑 바꿀 때, 단순히 아래로 내림
                self.percolate_down(deleteNode) 
            
            # finally 
            self.size = self.size - 1
            if(self.size < 2 ** (self.height+1)):
                self.height = self.height - 1 # 높이 업데이트
                
            return
        
                
if __name__ == "__main__":
    import random
    Data = [random.randint(1,1001) for _ in range(1,16)]
    def Heap_Test():
        print("원래 데이터: ")
        print(Data, end="\n")
        print("힙 테스트 시작 ")
        heap = Heap("minHeap") 
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
        heap.nodeSearch(Data[-1])
        print("노드 값 찾기 (없는 값):" + str(1010))
        heap.nodeSearch(1010)
        print()
        heap.height = heap.treeHeight(heap.root)
        print("힙의 높이: " + str(heap.height))
        print("트리에서 노드 지우기 (5번째 값): " + str(Data[5]))
        heap.nodeDelete(Data[5])
        print("삭제하고 힙 구조: ")
        heap.printAll()
        print("힙에서 노드 지우기 (1번째 값): " + str(Data[1]))
        heap.nodeDelete(Data[1])
        print("삭제하고 힙 구조: ")
        heap.printAll()
        print("힙에서 노드 지우기 (루트 값): " + str(heap.root.data))
        heap.nodeDelete(heap.root.data)
        print("삭제하고 힙 구조: ")
        heap.printAll()
        print("힙 테스트 이상 무")
    Heap_Test()
    print("----------------------------------------")
