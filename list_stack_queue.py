class Linked_List_Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class Linked_List():
    def __init__(self):
        self.head = None
        self.current = None
        self.pre = None
        self.size = 0  
    
    def printAll(self):
        list = []
        self.current = self.head
        while self.current.next != None:
            list.append(self.current.data)
            self.current = self.current.next
        list.append(self.current.data)
        for i in range(0, self.size):
            print(list[i], end="->")
        print()
        
        
    def nodeAdd(self, data): # 노드를 끝에 추가
        newNode = Linked_List_Node(data)
        if(self.head == None): # 빈 리스트일 시 초기화
            self.head = newNode
            self.current = newNode
            self.pre = newNode
            self.size = self.size + 1
        else: # 노드가 1개 이상일시 끝에 추가
            self.current = self.head
            while self.current.next != None:
                self.current = self.current.next
            self.current.next = newNode
            newNode.prev = self.current 
            self.size = self.size + 1
            
    
    def nodeInsert(self, data, index): # 노드를 index(0~size-1)에 추가
        newNode = Linked_List_Node(data)
        if(index < 0 or index > self.size - 1):
            print("index가 list 범위에서 벗어났습니다. 가능 범위: 0 ~ %d" % (self.size-1))
            return
        elif(index == 0):
            self.current = self.head
            self.head = newNode
            self.current.prev = newNode
            newNode.next = self.current
            self.size = self.size + 1
            
        elif(index == (self.size - 1)):
            self.nodeAdd(data)
            
        else: 
            count = 0
            self.current = self.head
            while(count != index):
                self.current = self.current.next
                count = count + 1
            self.pre = self.current.prev
            self.pre.next = self.current.prev = newNode
            newNode.prev = self.pre
            newNode.next = self.current
            self.size = self.size + 1
    
    def nodeSearch(self, data):
        self.current = self.head
        while self.current.next != None:
            if(self.current.data != data):
                self.current = self.current.next
            else:
                print("값을 찾았습니다.")
                return True
        if(self.current.data == data): # 마지막에 값이 있는 경우
            print("마지막에서 값을 찾았습니다.") 
            return True
        else:
            print("값이 리스트에 없습니다.")
            return False   
    
    def nodeDelete(self, data):
        if(self.nodeSearch(data) == False):
            return
        else:
            self.current = self.head
            while self.current.next != None:
                if(self.current.data != data):
                    self.current = self.current.next
                else:
                    break
            if(self.size == 1): # 요소가 한 개 밖에 없을 경우
                self.head = None
                del self.current
                self.pre = self.current = None
                self.size = self.size - 1
                
            else: # 요소가 2개 이상일 경우
                if(self.current == self.head): # 헤드 케이스
                    self.head = self.current.next
                    self.current.next.prev = None
                    self.current.next = None
                    del self.current
                    self.size = self.size - 1
                    
                elif(self.current.next == None): # 꼬리 케이스
                    self.pre = self.current.prev
                    self.current.prev = None
                    self.pre.next = None
                    del self.current
                    self.size = self.size - 1
                    
                else: # 중간 케이스
                    self.pre = self.current.prev 
                    self.pre.next = self.current.next
                    self.current.next.prev = self.pre
                    del self.current
                    self.size = self.size - 1
            
class Stack():
    def __init__(self, limit):
        self.limit = limit
        self.size = 0
        self.top = None
        self.stack = Linked_List()    
        
    def isStackFull(self):
        if(self.size == self.limit):
            return True
        else:
            return False
        
    def isStackEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False
        
    def push(self, data):
        if(self.isStackFull()):
            print("스택이 가득차 푸시 할 수 없습니다.")
            return
        else:
            self.stack.nodeAdd(data)
            self.top = data
            self.size = self.size + 1
            print("푸시 성공")
            
    def pop(self):
        if(self.isStackEmpty()):
            print("스택이 비어서 팝할 수 없습니다.")
            return
        else:
            self.stack.nodeDelete(self.top) # 마지막 노드 삭제
            pop_value = self.top
            if(self.stack.size == 0):
                self.top = None
            else:
                self.top = self.stack.pre.data # 마지막 요소 교체
            self.size = self.size - 1
            print("팝 성공")
            return pop_value
        
    def peek(self): #top위치 데이터 확인
        if(self.isStackEmpty()):
            print("스택이 비었습니다.")
            return
        else:
            return self.top
    
    def printAll(self):
        if(self.isStackEmpty()):
            print("스택이 비었습니다.")
            return
        else:
            list = []
            self.stack.current = self.stack.head
            while self.stack.current.next != None:
                list.append(self.stack.current.data)
                self.stack.current = self.stack.current.next
            list.append(self.stack.current.data)
            for i in range(self.stack.size-1, -1 , -1):
                if(i == (self.size-1)):
                    print(str(list[i]) + "<- top", end="\n")
                else:
                    print(list[i], end="\n")
            print()
            
class Queue(): # circular
    def __init__(self, limit):
        self.limit = limit
        self.size = 0
        self.front = None
        self.rear = None
        self.queue = Linked_List()
        
    def isQueueFull(self):
        if(self.size == self.limit):
            return True
        else:
            return False
    
    def isQueueEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False
    
    def enqueue(self, data): # rear위치에 노드 추가
        if(self.isQueueFull()):
            print("큐가 가득차 인큐 할 수 없습니다.")
            return
        else:
            self.queue.nodeAdd(data)
            self.rear = data
            if(self.size == 0):
                self.front = data
            else: # size가 1이상일 경우
                pass 
            self.size = self.size + 1
            print("인큐 성공")
        
    def dequeue(self): # front 위치에 노드 감소
        if(self.isQueueEmpty()):
            print("큐가 비어서 디큐할 수 없습니다.")
            return
        else:
            self.queue.nodeDelete(self.front) # 첫번째 노드 삭제
            dequeue_value = self.front
            if(self.queue.size == 0): # size가 없을 경우 front 초기화
                self.front = None
            else:
                self.front = self.queue.head.data # 첫번째 요소 교체
            self.size = self.size - 1
            print("디큐 성공")
            return dequeue_value
        
    def peek(self): # front위치 데이터 출력
        if(self.isQueueEmpty()):
            print("큐가 비었습니다.")
            return
        else:
            return self.front
        
    def printAll(self): # 모든 데이터 출력
        if(self.isQueueEmpty()):
            print("큐가 비었습니다.")
            return
        else:
            list = []
            self.queue.current = self.queue.head
            while self.queue.current.next != None:
                list.append(self.queue.current.data)
                self.queue.current = self.queue.current.next
            list.append(self.queue.current.data)
            for i in range(self.queue.size-1, -1 , -1):
                if(i == (self.size-1)):
                    print(str(list[i]) + "<- rear", end="\n")
                elif(i == 0):
                    print(str(list[i]) + "<- front", end="\n")
                else:
                    print(list[i], end="\n")
            print()
            
if __name__ == "__main__":
    import random
    Data = [random.randint(1,100) for _ in range(1,11)]
    def Linked_List_Test():
        print("원래 데이터: ")
        print(Data, end="\n")
        print("리스트 테스트 시작 ")
        linked_list = Linked_List()
        print("리스트에 모든 요소 추가함")
        for i in range(0, len(Data)):
            linked_list.nodeAdd(Data[i]) # 노드에 하나씩 추가
        print("리스트 추가 후: ")
        linked_list.printAll()
        print("리스트 삽입: 오류케이스")
        linked_list.nodeInsert(25, 14) # 오류 케이스
        linked_list.nodeInsert(25, 5) # 정상 케이스
        print("리스트 삽입 후(5번째): ")
        linked_list.printAll()
        print("리스트 요소 삭제 에러 케이스: ")
        linked_list.nodeDelete(101) # 없는 값 삭제 시도
        print("리스트 요소 삭제(5번째): ")
        linked_list.nodeDelete(25) # 삭제
        linked_list.printAll()
        print("리스트 요소 삽입(0번째)): ")
        linked_list.nodeInsert(105, 0) # 헤드 삽입 케이스
        print("리스트 삽입 후(0번째): ")
        linked_list.printAll()
        print("리스트 요소 삽입(마지막)): ")
        linked_list.nodeInsert(102, 10) # 테일 삽입 케이스
        print("리스트 삽입 후(마지막): ")
        linked_list.printAll()
        print("리스트 요소 삭제(0번째): ")
        linked_list.nodeDelete(105) # 헤드 삭제
        linked_list.printAll()
        print("리스트 요소 삭제(마지막): ")
        linked_list.nodeDelete(102) # 테일 삭제
        linked_list.printAll()
        print("리스트 테스트 이상 무")
    Linked_List_Test()
    print("----------------------------------------")
    
    def Stack_Test():
        print("원래 데이터: ")
        print(Data, end="\n")
        print("스택 테스트 시작 ")
        stack = Stack(10) # limit == 10
        for i in range(0, len(Data)):
            stack.push(Data[i]) # 스택에 하나씩 추가
        print()
        print("스택 추가 후: ")
        stack.printAll()
        print("스택 삽입 오류케이스(1) 스택이 가득 참:")
        stack.push(101) # 오류 케이스
        print("스택  팝: ")
        pop_value = stack.pop()
        peek_value = stack.peek()
        print("팝 값:  %d" % pop_value)
        print("peek 값(pop후에 현재 top값): %d" % peek_value)
        print("현재 스택 상태 : ")
        stack.printAll()
        print("연속적으로 팝해서 비우기: ")
        for _ in range(9):
            pop_value = stack.pop() # 비우기
            print("팝 값:  %d" % pop_value)
        print("마지막까지 팝 완료")
        print("스택 팝 오류케이스: 빈 스택에 팝하기")
        stack.pop()
        print("현재 스택 상태 : ")
        stack.printAll()
        print("스택 테스트 이상 무")
    Stack_Test()
    print("----------------------------------------")
    
    def Queue_Test():
        print("원래 데이터: ")
        print(Data, end="\n")
        print("큐 테스트 시작 ")
        queue = Queue(10) # limit == 10
        for i in range(0, len(Data)):
            queue.enqueue(Data[i]) # 큐에 하나씩 추가
        print()
        print("큐 추가 후: ")
        queue.printAll()
        print("큐 삽입 오류케이스(1) 큐이 가득 참:")
        queue.enqueue(101) # 오류 케이스
        print("큐  디큐: ")
        dequeue_value = queue.dequeue()
        peek_value = queue.peek()
        print("큐 값:  %d" % dequeue_value)
        print("peek 값(dequeue후에 현재 front값): %d" % peek_value)
        print("현재 큐 상태 : ")
        queue.printAll()
        print("연속적으로 디큐해서 비우기: ")
        for _ in range(9):
            dequeue_value = queue.dequeue() # 비우기
            print("팝 값:  %d" % dequeue_value)
        print("마지막까지 디큐 완료")
        print("큐 팝 오류케이스: 빈 큐에 디큐하기")
        queue.dequeue()
        print("현재 큐 상태 : ")
        queue.printAll()
        print("큐 테스트 이상 무")
    Queue_Test()
    print("----------------------------------------")
            
        