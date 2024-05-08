class Graph(): # directed(dfs), , dynamic add
    def __init__(self):
        self.size = 0
        self.vertex = [] # V(G) = [A,B,C,D] # char data추가
        self.edge = [] # E(G) = [[src, dst]] -> 참조: self.edge[순서][0] == src, self.edge[순서][1] == dst(GraphNode)
        self.adjacency_matrix = None # edgeConnect하고 호출해서 생성
        
    def nodeAdd(self, data):
        if(data == None):
            return
        
        else:
            self.vertex.append(data)
            self.size = self.size + 1
            return  
        
    def nodeInsert(self, data, edge):
        
        if(data not in self.vertex):
            self.nodeAdd(data)
            
        for i in range(len(edge)):
            if(edge[i][0] == data or edge[i][1] == data):
                pass
            
            else:
                print("edge가 해당 노드를 대상으로 하지 않습니다.")
                return
            
        self.edge += edge # edgeConnect
        self.build_adjacency_matrix() 
        
        return
    
    def nodeDelete(self, data):
        
        if(data not in self.vertex):
            print("삭제하려는 값이 그래프에 없습니다.")
            return
    
        else: # insert의 역순: edge를 끊고 nodeAdd를 반대로
            delete_candidate = []
            for i in range(len(self.edge)):
                if(self.edge[i][0] == data or self.edge[i][1] == data): # edge의 구성요소인 경우
                    delete_candidate.append(self.edge[i]) #지울 위치의 내용물을 담음
            
            for i in range(len(delete_candidate)):
                self.edge.remove(delete_candidate[i]) # self.edge에서 제거(edge는 중복 x)
                
            self.vertex.remove(data) # vertex집합에서 제거   
            self.size = self.size - 1
            # 끊고 재구성
            self.build_adjacency_matrix()
            return
            
        
    def edgeConnect(self, src, dst): # src->dst인 edge를 self.edge에 추가한다.
        if src == None or dst == None:
            print("출발지나 목적지가 없습니다.")
            return
        
        else:
            edge = [src, dst]
            self.edge.append(edge)
            return
    
    def build_adjacency_matrix(self): # 삽입이나 삭제를 해도 처음부터 그래프 재구성함
        def findIdxByname(data):
            Idx = 0
            for i in range(len(self.vertex)):
                if(self.vertex[i] == data):
                    Idx = i
                    break
                
            return Idx
        
        if(self.vertex != [] and self.edge != []):
            adjacency_matrix = [[0 for _ in range(self.size)] for _ in range(self.size)] # 0으로 초기화
            for i in range(len(self.vertex)):
                for j in range(len(self.edge)):
                    if(self.vertex[i] == self.edge[j][0]): # edge src와 vertex row가 같으면
                        dst = self.edge[j][1]
                        Idx = findIdxByname(dst)
                        adjacency_matrix[i][Idx] = 1
                        
            self.adjacency_matrix = adjacency_matrix
            
            return 
            
        else:
            print("노드가 없거나 노드 간 연결이 없습니다.")
            return
        
    def print_adjacency_matrix(self):
    
        for i in range(len(self.vertex)+1):
            for j in range(len(self.vertex)+1):
                if(i == 0 and j == 0): # 첫 칸
                    print(" ", end=" ")
                elif(i == 0 and j != 0): # 첫 row
                    print("%c" % self.vertex[j-1], end=" ")
                elif(i != 0 and j == 0): # 첫 column
                    print("%c" % self.vertex[i-1], end=" ")
                else: # 나머지는 내용 첨부
                    print("%d" % self.adjacency_matrix[i-1][j-1], end=" ")
                    
            print() # 한 줄 끝나고 띄움 
            
    def DFS(self): 
        
        stack = []
        visitedAry = []
        current = 0
        stack.append(current) # 최근 방문한 순서부터 깊이 들어가기, Idx를 담음 
        visitedAry.append(self.vertex[current]) # 방문한 노드들, 실제 노드 data를 담음
        
        while(len(stack) != 0):
            next = None
            for vertex in range(self.size):
                if self.adjacency_matrix[current][vertex] == 1: # 현재 노드에서 이어져있다면
                    if self.vertex[vertex] in visitedAry: # 방문했다면 넘어감
                        pass 
                    
                    else: # 방문 안했다면
                        next = vertex
                        break
                    
            if next != None: # 다음 방문할 장소를 찾았다면
                current = next
                stack.append(current)
                visitedAry.append(self.vertex[current])
            else: # 방문할 장소가 더이상 없다면
                current = stack.pop()
                    
        
        return visitedAry # 방문한 순서 리턴
    
    def BFS(self): 
        
        queue = []
        visitedAry = []
        current = 0
        queue.append(current) # 최근 방문한 순서부터 인접한 노드들을 담음, Idx를 담음 
        visitedAry.append(self.vertex[current]) # 방문한 노드들, 실제 노드 data를 담음
        
        while(len(queue) != 0):
            for vertex in range(self.size):
                if self.adjacency_matrix[current][vertex] == 1: # 현재 노드에서 이어져있다면
                    if self.vertex[vertex] in visitedAry: # 방문했다면 넘어감
                        pass
                    
                    else: # 방문 안했다면 큐랑 방문장소에 집어넣음
                        queue.append(vertex)
                        visitedAry.append(self.vertex[vertex])
                        
                if(vertex == (self.size -1)): # 끝에 와서 방문할 장소가 더이상 없다면 디큐
                    current = queue[0]
                    del queue[0]
                        
        return visitedAry # 방문한 순서 리턴
    
    

        
if __name__ == "__main__":
    import random
    import string # 문자로 이루어진 그래프 노드
    Data = random.sample(string.ascii_letters,10) # ascii문자들 중 10개를 랜덤으로 뽑는다.
    # random.sample은 중복되지 않게 추출한다.
    print("원래 데이터: ")
    print(Data)
    def graph_Test():
        graph = Graph()
        print("그래프 노드 생성: ")
        for i in range(len(Data)):
            graph.nodeAdd(Data[i])
        print(graph.vertex)    
        print()
        
        print("랜덤 edge 연결: ") # 최대 10*9 = 90개
        for i in range(65):
            random_sample = random.sample(graph.vertex, 2) # vertex집합에서 2개 중복미허용으로 뽑음(원본은 유지)
            src = random_sample[0] #랜덤 src값
            dst = random_sample[1] #랜덤 dst값
            if([src, dst] not in graph.edge): # 이미 추가한 edge 조합이 아닐 때
                graph.edgeConnect(src, dst) 
        print(graph.edge)
        print("엣지 개수 " + str(len(graph.edge)))
        print()
        
        print("인접 그래프 생성 및 출력: (row가 src, col이 dst)")
        graph.build_adjacency_matrix() # 여기까지가 그래프 초기화 단계
        graph.print_adjacency_matrix()
        print()
        print("그래프 사이즈: %d" % graph.size)
        print()
        
        print("그래프 순회1 DFS: ")
        dfs_order = graph.DFS()
        for i in range(len(dfs_order)):
            if(i == len(dfs_order)-1):
                print("%c" % dfs_order[i])
            else:
                print("%c" % dfs_order[i], end="->")
        print()
            
        print("그래프 순회2 BFS: ")
        bfs_order = graph.BFS()
        for i in range(len(bfs_order)):
            if(i == len(bfs_order)-1):
                print("%c" % bfs_order[i])
            else:
                print("%c" % bfs_order[i], end="->")
        print()
        
        print("그래프 노드 삽입: (값: 랜덤, edge: 랜덤)")
        # 제외할 문자를 제외한 나머지 문자들로 구성된 새로운 문자열을 생성합니다.
        valid_chars = ''.join(char for char in string.ascii_letters if char not in graph.vertex)
        # 샘플링할 문자를 생성합니다.
        sampled_char = random.sample(valid_chars, 1)
        sampled_char = sampled_char[0]
        # 해당 문자를 src나 dst로 하는 edge를 임의로 만듭니다.
        edge = []
        for i in range(4):
            random_sample = random.sample(graph.vertex, 1) 
            src = sampled_char
            dst = random_sample[0]
            edge.append([src, dst])
            
        for _ in range(4):
            random_sample = random.sample(graph.vertex, 1) 
            src = random_sample[0]
            dst = sampled_char
            edge.append([src, dst])
        graph.nodeInsert(sampled_char, edge)
        print("그래프 삽입 후 출력: ")
        graph.print_adjacency_matrix()
        
        print("그래프 노드 삭제(5번째 vertex): %c" % graph.vertex[5])
        graph.nodeDelete(graph.vertex[5])
        print("그래프 삭제 후 출력: ") 
        graph.print_adjacency_matrix()
        print()
    graph_Test()
    print("----------------------------------------")