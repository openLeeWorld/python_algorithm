from heap import *

class Sort():
    def __init__(self, mode): # mode는 오름차순(True) or 내림차순(False)
        self.mode = mode

    def bubble_sort(self, data): # 양 옆을 비교해서 끝으로 계속 보냄
        sorted_data = data[:]
        n = len(Data)
        if(self.mode == True):
            for end in range(n-1, 0, -1):
                changed = False
                for cur in range(0, end):
                    if(sorted_data[cur] > sorted_data[cur+1]):
                        sorted_data[cur], sorted_data[cur+1] = sorted_data[cur+1], sorted_data[cur]
                        changed = True
                        
                if not changed:
                    break
                
        else:
            for end in range(n-1, 0, -1):
                changed = False
                for cur in range(0, end):
                    if(sorted_data[cur] < sorted_data[cur+1]):
                        sorted_data[cur], sorted_data[cur+1] = sorted_data[cur+1], sorted_data[cur]
                        changed = True
                        
                if not changed:
                    break
                
        return sorted_data 
    
    def selection_sort(self, data): # min max을 계속 뽑아냄
        before = data[:]
        sorted_data = []
        
        def findMinIdx(data):
            minIdx = 0
            for i in range(1, len(data)):
                    if(data[minIdx] > data[i]):
                        minIdx = i 
                        
            return minIdx
        
        def findMaxIdx(data):
            maxIdx = 0
            for i in range(1, len(data)):
                    if(data[maxIdx] < data[i]):
                        maxIdx = i 
                        
            return maxIdx
        
        if(self.mode == True):
            for _ in range(len(data)):
                minPos = findMinIdx(before)
                sorted_data.append(before[minPos])
                del(before[minPos])
                
        else:
            for _ in range(len(data)):
                maxPos = findMaxIdx(before)
                sorted_data.append(before[maxPos])
                del(before[maxPos])
                
        return sorted_data 
    
    def insertion_sort(self, data): # 요소를 골라서 맞는 위치까지 보냄
        sorted_data = data[:]
        n = len(data)
        if(self.mode == True):
            for end in range(1, n):
                for cur in range(end, 0, -1):
                    if(sorted_data[cur-1] > sorted_data[cur]):
                        sorted_data[cur-1], sorted_data[cur] = sorted_data[cur], sorted_data[cur-1]
                        
            return sorted_data
        
        else:
            for end in range(1, n):
                for cur in range(end, 0, -1):
                    if(sorted_data[cur-1] < sorted_data[cur]):
                        sorted_data[cur-1], sorted_data[cur] = sorted_data[cur], sorted_data[cur-1]
                        
        return sorted_data 
    
    def heap_sort(self, data):
        sorted_data = []
        if(self.mode == True):
            heap = Heap("minHeap")
            for i in range(len(data)):
                heap.nodeAdd(data[i])
                
            for i in range(len(data)):
                min_value = heap.returnRoot()
                sorted_data.append(min_value)
                heap.nodeDelete(min_value)
        else:
            heap = Heap("maxHeap")
            for i in range(len(data)):
                heap.nodeAdd(data[i])
                
            for i in range(len(data)):
                max_value = heap.returnRoot()
                sorted_data.append(max_value)
                heap.nodeDelete(max_value)
                
        return sorted_data 
    
    def merge_sort(self, data):
        previous_data = data[:]

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if self.mode:
                    if left[i] <= right[j]:
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                else:
                    if left[i] >= right[j]:
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        def divide_and_merge(data):
            if len(data) <= 1:
                return data

            mid = len(data) // 2
            left = divide_and_merge(data[:mid])
            right = divide_and_merge(data[mid:])

            return merge(left, right)

        return divide_and_merge(previous_data)

    def quick_sort(self, data):
        previous_data = data[:] # shallow copy() : 불변 객체는 복사, 변형 객체는 같은 메모리 참조(동적 할당) <-> deep copy(copy.deepcopy())
        
        def qsort(arr, start, end):
            if(start >= end):
                return 
            
            low = start
            high = end
            pivot = arr[(low + high) // 2]
            
            if(self.mode == True): # 오름차순
                while low <= high:
                    while arr[low] < pivot:
                        low+=1
                    while arr[high] > pivot:
                        high-=1
                    if low <= high:
                        arr[low], arr[high] = arr[high], arr[low]
                        low,high = low+1, high-1
                        
            elif(self.mode == False): # 내림차순
                while low <= high:
                    while arr[low] > pivot:
                        low+=1
                    while arr[high] < pivot:
                        high-=1
                    if low <= high:
                        arr[low], arr[high] = arr[high], arr[low]
                        low,high = low+1, high-1    
                    
            mid = low
            qsort(arr, start, mid-1) 
            qsort(arr, mid, end)       
            
        qsort(previous_data, 0, len(previous_data)-1)
    
        return previous_data
        
if __name__ == "__main__":
    import random
    Data = [random.randint(1,1001) for _ in range(1,20)]
    def Sort_Test():
        print("원래 데이터: ")
        print(Data, end="\n")
        print("정렬 테스트 시작 ")
        sort = Sort(True)
        print("오름차순: ")
        print("내장함수 결과: ")
        Data_sorted = sorted(Data)
        print(Data_sorted)
        print("bubble sort 결과:")
        Data_bubble = sort.bubble_sort(Data)
        print(Data_bubble)
        print("selection sort 결과: ")
        Data_selection = sort.selection_sort(Data)
        print(Data_selection)
        print("insertion sort 결과: ")
        Data_insertion = sort.insertion_sort(Data)
        print(Data_insertion)
        print("heapsort 결과: ")
        Data_heap = sort.heap_sort(Data)
        print(Data_heap)
        print("mergesort 결과: ")
        Data_merge = sort.merge_sort(Data)
        print(Data_merge)
        print("quicksort 결과: ")
        Data_quick = sort.quick_sort(Data)
        print(Data_quick)
        print()
        print("내림차순: ")
        sort = Sort(False)
        print("내장함수 결과: ")
        Data_sorted = sorted(Data, reverse=True)
        print(Data_sorted)
        print("bubble sort 결과:")
        Data_bubble = sort.bubble_sort(Data)
        print(Data_bubble)
        print("selection sort 결과: ")
        Data_selection = sort.selection_sort(Data)
        print(Data_selection)
        print("insertion sort 결과: ")
        Data_insertion = sort.insertion_sort(Data)
        print(Data_insertion)
        print("heapsort 결과: ")
        Data_heap = sort.heap_sort(Data)
        print(Data_heap)
        print("mergesort 결과: ")
        Data_merge = sort.merge_sort(Data)
        print(Data_merge)
        print("quicksort 결과: ")
        Data_quick = sort.quick_sort(Data)
        print(Data_quick)
        print("정렬 테스트 이상 무")
    Sort_Test()
    print("----------------------------------------")
