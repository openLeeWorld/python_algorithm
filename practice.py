data = 1
print("--%d" % data, end="\n")
print("  ", end="")
print("|", end="")
print("--%d" % data, end="\n")
print("  ", end="")
print("|", end="")
print("--%d" % data, end="\n")

edge = [] # E(G) = [{src: dst}, {src2: dst2}] -> 참조: self.edge[0] == {src: dst}, dictionary
edge.append(["src", "dst"])
print(edge[0][0])

import string 
import random

letters_set = string.ascii_letters
print(letters_set)

random_list = random.sample(letters_set,10)
print(random_list)

lists = [[5,6], [1,2], [5,6]]
if([1,1] not in lists):
    print("in 성공")

practice_list = [1,2,3]
del practice_list[0]
practice_list.remove(2)
print(practice_list)

Data = random.randint(1,101)
print(Data)

class WeightedEdge(): # edge.weight > 0 
    def __init__(self, vertex_set, weight):
        self.vertex_set = vertex_set # [A,B]
        self.weight = weight # 양수
        
list_s = []
for _ in range(6):
    random_sample = random.sample(string.ascii_letters, 2) # vertex집합에서 2개 중복미허용으로 뽑음(원본은 유지)
    # weight도 랜덤하게 넣음
    weight = random.randint(1,101)
    edge = WeightedEdge(random_sample, weight) 
    list_s.append(edge)
    
srt = sorted(list_s, key= lambda edge: edge.weight, reverse=True)
print([[srt[i].vertex_set, srt[i].weight] for i in range(len(srt))])

from math import inf
infinity = [inf]
print(infinity[0])

list_a =[1,2,3]
print(random.choice(list_a))