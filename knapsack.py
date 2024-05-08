from sort import Sort

class Knapsack(): # memoization and dynamic programming: 가방 무게를 안 넘는 선에서 넣을 물건들의 가치의 합이 최대가 되도록 하라
    def __init__(self, limit):
        self.limit = limit # 가방 무게
    
    def solve(self, value, weight):
        # memoization array
        maxWeight = self.limit
        rowCount = len(weight)
        array = [[[0, 0] for _ in range(maxWeight+1)] for _ in range(rowCount+1)] # [current_value, current_weight]
        for row in range(1, rowCount+1):
            for col in range(1, maxWeight + 1):
                if weight[row-1] > col: # 내가 안들어가면
                    array[row][col] = array[row-1][col] # 추가 안하고 (그 전 무게까지의 데이터)
                else: # 들어가면
                    if(weight[row-1] + array[row-1][col][1] <= maxWeight): # 왼쪽과 위 세트가 둘 다 들어갈 때(왼쪽을 추가)
                        array[row][col][1] = weight[row-1] + array[row-1][col][1]
                        array[row][col][0] = value[row-1] + array[row-1][col][0]
                    
                    else: # 둘 세트가 안들어가서 왼쪽이나 위 중 하나를 선택해야 할 때
                        value1 = array[row][col-1][0] # 왼쪽
                        value2= array[row-1][col][0] # 오른쪽
                        max_value = max(value1, value2)
                        
                        if(max_value == value1): # 왼쪽 추가시
                            array[row][col][1] = array[row][col-1][1] 
                            array[row][col][0] = max_value
                                
                        elif(max_value == value2): # 위쪽 추가시
                            array[row][col][1] = array[row-1][col][1] 
                            array[row][col][0] = max_value 
                    
        return array[rowCount][maxWeight] # 최고 무게상황에서의 최고 가치 반환
        
    
if __name__ == "__main__":
    import random
    value = [random.randint(1,11) for _ in range(1,6)]  # 각 물건의 가치
    weight = [random.randint(1,11) for _ in range(1,6)] # 각 물건의 가격
    def knapsack_Test():
        knapsack = Knapsack(20)
        sort = Sort(False) # 가치가 높은 것부터 넣어봄
        value_sorted = sort.quick_sort(value)
        print("각 물건의 가치: ")
        print(value_sorted, end="\n")
        print("각 물건의 무게: ")
        print(weight, end="\n")
        best_value = knapsack.solve(value_sorted, weight)
        print("최고 가치 솔루션: %d" % best_value[0])
        print("현재 무게: %d" % best_value[1])
    knapsack_Test()
    print("----------------------------------------")
    
    