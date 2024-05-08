from graph import *
import copy
from math import inf
#weighted, undirected graph
class WeightedEdge(): # edge.weight > 0 
    def __init__(self, vertex_set, weight):
        self.vertex_set = vertex_set # [A,B]
        self.weight = weight # 양수        

class WeightedGraph(Graph):
    def edgeConnect(self, src, dst, weight): # [src, dst]인 edge를 self.edge에 추가한다.
        if src == None or dst == None:
            print("출발지나 목적지가 없습니다.")
            return
        
        else:
            vertex_set = [src, dst] # undirected이긴 하지만..
            edge = WeightedEdge(vertex_set, weight)
            if(edge not in self.edge): # 이미 추가한 edge 조합이 아닐 때
                self.edge.append(edge)
                
            return
        
    def build_adjacency_matrix(self): # 삽입이나 삭제를 해도 처음부터 그래프 재구성함
        def findIdxByname(data):
            Idx = inf
            for i in range(len(self.vertex)):
                if(self.vertex[i] == data):
                    Idx = i
                    break
                
            return Idx
        
        if(self.vertex != [] and self.edge != []):
            adjacency_matrix = [[0 for _ in range(self.size)] for _ in range(self.size)] # 0으로 초기화
            for i in range(len(self.vertex)):
                for j in range(len(self.edge)):
                    if(self.vertex[i] == self.edge[j].vertex_set[0]): # edge src와 vertex row가 같으면
                        dst = self.edge[j].vertex_set[1]
                        Idx = findIdxByname(dst)
                        adjacency_matrix[i][Idx] = 1
                        adjacency_matrix[Idx][i] = 1
                        
            self.adjacency_matrix = adjacency_matrix
            
            return 
            
        else:
            print("노드가 없거나 노드 간 연결이 없습니다.")
            return
        
    def nodeInsert(self, data, edge):
        
        if(data not in self.vertex):
            self.nodeAdd(data)
                
        for i in range(len(edge)):
            if(edge[i].vertex_set[0] == data or edge[i].vertex_set[1] == data):
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
                if(self.edge[i].vertex_set[0] == data or self.edge[i].vertex_set[1] == data): # edge의 구성요소인 경우
                    delete_candidate.append(self.edge[i]) #지울 위치의 내용물을 담음
            
            for i in range(len(delete_candidate)):
                self.edge.remove(delete_candidate[i]) # self.edge에서 제거(edge는 중복 x)
                
            self.vertex.remove(data) # vertex집합에서 제거   
            self.size = self.size - 1
            # 끊고 재구성
            self.build_adjacency_matrix()
            return
        
    def kruskal(self): # edge weight를 내림차순으로 정렬한 뒤 큰 거부터 하나씩 제거하면서 traversal이 모두 되는지 확인하다. (E = V-1까지 반복)
        dfs_order = self.DFS()
        if(len(dfs_order) != len(self.vertex)):
            print("원래 그래프가 스패닝 트리가 아닙니다.")
            return
        
        else:
            # spanning tree조작을 위해 그래프 값을 복사한다.
            graph = copy.deepcopy(self)
            E = len(graph.edge)
            V = len(graph.vertex)
            graph.edge.sort(key= lambda edge: edge.weight, reverse=True) # edge클래스들이 weight 큰 순으로 정렬됨, 복사됨
            #print("가중치에 따라 에지 정렬: ")
            #print([[graph.edge[i].vertex_set, graph.edge[i].weight] for i in range(len(graph.edge))])
            while(E > V - 1):
                max_weight_edge = graph.edge[0]
                graph.edge.remove(max_weight_edge)
                graph.build_adjacency_matrix() # edge를 지우고 새로 그래프 생성
                dfs_order = graph.DFS()
                if(len(dfs_order) != len(graph.vertex)):
                    # edge를 지우면 연결이 끊어지므로 복구하고 끝냄
                    graph.edge.insert(0, max_weight_edge)
                    graph.build_adjacency_matrix() # edge를 넣고 새로 그래프 생성
                    break
                else:
                    # 안 끊어지면 끊고 다음 while로 진행
                    E = E - 1
                    
            print()        
            print("krusal결과에 의한 spanning tree: ")
            graph.print_adjacency_matrix()
            
            cost = 0 # minimum spanning tree의 cost
            for i in range(len(graph.edge)): # 남은 에지들을 돌면서 cost계산
                cost += graph.edge[i].weight
            
            del graph
            return cost
        
    def prims(self): # 첫 정점에서 시작하여 가장 작은 간선을 가진 이웃을 신장 트리 집합에 추가해나간다. (모든 정점이 추가될 때 까지)
        
        stack = [] # 방문 노드 인덱스를 스택으로 저장
        visitedAry = [] # 방문 노드 집합
        current = 0 # 루트부터 시작
        stack.append(current) # 최근 방문한 순서부터 깊이 들어가기, Idx를 담음 
        visitedAry.append(self.vertex[current]) # 방문한 노드들, 실제 노드 data를 담음
        cost = 0
        graph = copy.deepcopy(self)
        graph_edge = []
        
        while(len(stack) != 0):
            nextCandidate = []
            min_weight = inf
            for vertex in range(graph.size):
                if graph.adjacency_matrix[current][vertex] == 1: # 현재 노드에서 이어져있다면
                    if graph.vertex[vertex] in visitedAry: # 방문했다면 넘어감
                        pass 
                    
                    else: # 방문 안했다면 후보에 추가
                        nextCandidate.append(vertex)
                        
                    if(vertex == (graph.size -1)):
                        break
                
                    
            if nextCandidate != []: # 다음 방문할 장소를 찾았다면 각 노드로 가는 에지 값 중 최소를 선택하고 그 노드로 이동
                for n in range(len(nextCandidate)):
                    next = nextCandidate[n]
                    for i in range(len(graph.edge)):
                        if((graph.edge[i].vertex_set[0] == graph.vertex[current] and graph.edge[i].vertex_set[1] == graph.vertex[next])
                        or (graph.edge[i].vertex_set[0] == graph.vertex[next] and graph.edge[i].vertex_set[1] == graph.vertex[current])): 
                            
                            weight = self.edge[i].weight 
                            
                            if(min_weight > weight):
                                min_weight = weight
                                min_next_edge = i
                                min_next_vertex = next
                                
                        else:
                            pass
                        
                #최소 노드를 찾은 후 그 쪽으로 가기                
                cost += min_weight
                graph_edge.append(graph.edge[min_next_edge])
                
                stack.append(min_next_vertex)
                visitedAry.append(graph.vertex[min_next_vertex])
                current = min_next_vertex
                
            else: # 방문할 장소가 더이상 없다면
                current = stack.pop()
        
        print()     
        graph.edge = graph_edge   
        print("prims결과에 의한 spanning tree: ")
        graph.build_adjacency_matrix() 
        graph.print_adjacency_matrix()            
        del graph
        
        if(cost != inf):
            return cost # 최소 비용 리턴
        else:
            print("오류")
            return 
        
    def shortest_parth_dijkstra(self, source): # source
        def findIdxByname(data):
            Idx = inf
            for i in range(len(self.vertex)):
                if(self.vertex[i] == data):
                    Idx = i
                    break
            
            if(Idx != inf):    
                return Idx
            
            else:
                print("없는 노드 이름입니다.")
                return None
        
        def minIdxInUnvisited(unvisited_vertex, distance):
            minIdx = random.choice(unvisited_vertex)
                
            for i in unvisited_vertex: 
                if(distance[minIdx] > distance[i]): # 거리가 가장 작은 값
                    minIdx = i
                
            return minIdx
        
        def findNeighborOfu(u): # edge가 이어진 v(idx)를 찾는다. 
            v=[]
            
            for i in range(len(self.edge)):
                if(self.edge[i].vertex_set[0] == self.vertex[u]):
                    neighbor = self.edge[i].vertex_set[1]
                    neighborIdx = findIdxByname(neighbor)
                    if(neighborIdx not in v):
                        v.append(neighborIdx)
                    
                elif(self.edge[i].vertex_set[1] == self.vertex[u]):
                    neighbor = self.edge[i].vertex_set[0]
                    neighborIdx = findIdxByname(neighbor)
                    if(neighborIdx not in v):
                        v.append(neighborIdx)
                            
            return v
        
        def LengthOfuv(u, v): # u,v edge weight를 찾는다. (u, v는 인덱스)
            length = inf
            
            for i in range(len(self.edge)):
                if((self.edge[i].vertex_set[0] == self.vertex[u] and self.edge[i].vertex_set[1] == self.vertex[v])
                or (self.edge[i].vertex_set[0] == self.vertex[v] and self.edge[i].vertex_set[1] == self.vertex[u])):  # edge를 찾은 경우
                    length = self.edge[i].weight
                    break
                    
            return length
        
        distance = [] # 각 idx까지의 최소 거리 집합
        shortest_path = [] # 각 노드까지 최소 경로의 중간노드 집합(idx별 순서)
        unvisited_vertex = [] # 미방문 노드 인덱스 집합
        source_Idx = findIdxByname(source)
        prev = [inf for _ in range(len(self.vertex))] # 노드 상에서 최소 경로 상 바로 전 노드(인덱스 순서상), 소스로 초기화
        
        for i in range(len(self.vertex)):  #초기화
            distance.append(inf) 
            shortest_path.append([]) 
            unvisited_vertex.append(i)
            
        # 초기 소스 방문 처리
        distance[source_Idx] = 0 # 실제 weight
        shortest_path[source_Idx].append(source) # 실제 노드 이름 %c 
        prev[source_Idx] = 0
            
        while unvisited_vertex != []: # 모두 다 방문할때까지
            u = minIdxInUnvisited(unvisited_vertex, distance) # unvisited_vertex에서 가장 거리가 짧은 노드 index
            unvisited_vertex.remove(u) # u방문 처리
            # u의 각 이웃에 대해 
            v = findNeighborOfu(u) # u의 이웃집합
            for neighbor in v: # u의 각 이웃 v에 대해서
                length_uv = LengthOfuv(u, neighbor)
                alt = distance[u] + length_uv # edge relaxation
                    
                if alt < distance[neighbor]: # v의 각 요소까지의 거리보다 더 짧은 값을 찾을 시
                    distance[neighbor] = alt
                    prev[neighbor] = u
                        
        # 루프 탈출 후 경로를 복원한다(prev를 따라가는 길의 역순)
        
        for i in range(len(prev)): # len(prev) == len(self.vertex)
            if i != source_Idx: 
                path = [] # 각 노드마다의 경로
                path.append(i) # 도착지
                previous_node = prev[i] 
                while previous_node != 0: # 소스에 도달할 때까지
                    path.append(previous_node)
                    previous_node = prev[previous_node]
                    
                path.append(previous_node) #출발지 까지 담음
                path.reverse() # 출발지->도착지까지 역순으로 만듬
                nodepath = []
                for j in range(len(path)):
                    nodepath.append(self.vertex[path[j]])
                    shortest_path[i] = nodepath
            
        return distance, shortest_path
    
    def shortest_parth_bellman_ford(self, source): # 모든 vertex의 각 edge에 대해서 edge-relaxation을 해준다
        def findIdxByname(data):
            Idx = inf
            for i in range(len(self.vertex)):
                if(self.vertex[i] == data):
                    Idx = i
                    break
            
            if(Idx != inf):    
                return Idx
            
            else:
                print("없는 노드 이름입니다.")
                return None
            
        distance = []
        shortest_path = []
        source_Idx = findIdxByname(source)
        prev = [inf for _ in range(len(self.vertex))] # 노드 상에서 최소 경로 상 바로 전 노드(인덱스 순서상), 소스로 초기화
        
        for i in range(len(self.vertex)):  #초기화
            distance.append(inf) 
            shortest_path.append([])
            
        # 초기 소스 방문 처리
        distance[source_Idx] = 0 
        shortest_path[source_Idx].append(source) # 실제 노드 이름 %c 
        prev[source_Idx] = 0

        # repeat edge relaxation
        for i in range(len(self.vertex)):
            for j in range(len(self.edge)):
                src = self.edge[j].vertex_set[0] # src
                dst = self.edge[j].vertex_set[1] # dst
                weight = self.edge[j].weight
                src_idx = findIdxByname(src)
                dst_idx = findIdxByname(dst)
                if distance[dst_idx] > distance[src_idx] + weight:
                    distance[dst_idx] = distance[src_idx] + weight
                    prev[dst_idx] = src_idx
                # directed용이라 undirected용으로 두번 해봄    
                elif distance[src_idx] > distance[dst_idx] + weight:
                    distance[src_idx] = distance[dst_idx] + weight
                    prev[src_idx] = dst_idx
                    
        # 루프 탈출 후 경로를 복원한다(prev를 따라가는 길의 역순)
        
        for i in range(len(prev)): # len(prev) == len(self.vertex)
            if i != source_Idx: 
                path = [] # 각 노드마다의 경로
                path.append(i) # 도착지
                previous_node = prev[i] 
                while previous_node != 0: # 소스에 도달할 때까지
                    path.append(previous_node)
                    previous_node = prev[previous_node]
                    
                path.append(previous_node) #출발지 까지 담음
                path.reverse() # 출발지->도착지까지 역순으로 만듬
                nodepath = []
                for j in range(len(path)):
                    nodepath.append(self.vertex[path[j]])
                    shortest_path[i] = nodepath
        
        return distance, shortest_path
        
if __name__ == "__main__":
    import random
    import string # 문자로 이루어진 그래프 노드
    Data = random.sample(string.ascii_letters,20) # ascii문자들 중 10개를 랜덤으로 뽑는다.
    # random.sample은 중복되지 않게 추출한다.
    print("원래 데이터: ")
    print(Data)
    def weighted_graph_Test():
        graph = WeightedGraph()
        print("그래프 노드 생성: ")
        for i in range(len(Data)):
            graph.nodeAdd(Data[i])
        print(graph.vertex)    
        print()
        
        print("랜덤 edge 연결: ") # 최대 20*19 = 190개
        random_sample = []
        for i in range(100):
            sample = random.sample(graph.vertex, 2) # ascii문자들 중 20개를 랜덤으로 뽑는다.
            src = sample[0]
            dst = sample[1]
            if([dst, src] not in random_sample): # 순서 바꾼게 안에 있으면 넣지 않음
                random_sample.append(sample)
    
        for i in range(len(random_sample)):
            sample = random_sample[i]
            src = sample[0] #랜덤 src값
            dst = sample[1] #랜덤 dst값
            # weight도 랜덤하게 넣음
            weight = random.randint(1,101) # weight는 양수
            # edge를 만들어서 self.edge에 추가(있으면 자동으로 삭제됨)
            graph.edgeConnect(src, dst, weight) 
        
        #print(graph.edge)
        print("엣지 개수 " + str(len(graph.edge)))
        print()
        
        print("인접 그래프 생성 및 출력: (row가 src, col이 dst, src,dst가 없으므로 대칭임)")
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
        edges = []
        for i in range(4):
            random_sample = random.sample(graph.vertex, 1) 
            src = sampled_char
            dst = random_sample[0]
            weight = random.randint(1,101)
            edge = WeightedEdge([src, dst], weight)
            edges.append(edge)
            #대칭화
            src = random_sample[0]
            dst = sampled_char
            edge = WeightedEdge([src, dst], weight)
            edges.append(edge)
        graph.nodeInsert(sampled_char, edges)
        print("그래프 삽입 후 출력: ")
        graph.print_adjacency_matrix()
        print()
        
        print("그래프 노드 삭제(5번째 vertex): %c" % graph.vertex[5])
        graph.nodeDelete(graph.vertex[5])
        print("그래프 삭제 후 출력: ") 
        graph.print_adjacency_matrix()
        print()
        
        print("minimum spanning tree 생성: ")
        print("kruskal 알고리즘:" )
        min_cost = graph.kruskal()
        print("minimum cost는 %d입니다" % min_cost)
        print()
        
        print("prims 알고리즘:" )
        min_cost = graph.prims()
        print("minimum cost는 %d입니다" % min_cost)
        print()
        
        print("최단경로 알고리즘: (dijkstra) (출발점 루트: %c)" % graph.vertex[0])
        distance, shortest_path = graph.shortest_parth_dijkstra(graph.vertex[0]) 
        print("루트에서 각 노드까지의 최소 경로의 합: ")
        for i in range(len(distance)):
            print("%c:" % graph.vertex[i], end=" ")
            print(distance[i], end=", ")
        print()
        print("각 최종 노드까지의 중간 경로")    
        for i in range(len(shortest_path)):
            print("%c:" % graph.vertex[i], end=" ")
            length = len(shortest_path[i])
            for j in range(length):
                if(j == length-1):
                    print("%c" % shortest_path[i][j], end="\n")
                else:
                    print("%c" % shortest_path[i][j], end="->")
        print()
        
        print("최단경로 알고리즘: (bellman-Ford)(출발점 루트: %c)" % graph.vertex[0])
        distance, shortest_path = graph.shortest_parth_bellman_ford(graph.vertex[0])
        print("루트에서 각 노드까지의 최소 경로의 합: ")
        for i in range(len(distance)):
            print("%c:" % graph.vertex[i], end=" ")
            print(distance[i], end=", ")
        print()
        print("각 최종 노드까지의 중간 경로")    
        for i in range(len(shortest_path)):
            print("%c:" % graph.vertex[i], end=" ")
            length = len(shortest_path[i])
            for j in range(length):
                if(j == length-1):
                    print("%c" % shortest_path[i][j], end="\n")
                else:
                    print("%c" % shortest_path[i][j], end="->")
        print()
        
    weighted_graph_Test()
    print("----------------------------------------")