from sort import Sort
import time

class Search():
    def __init__(self, list):
        self.list = list # 찾을 집단 데이터
        self.size = len(list)
    
    def sequential_search(self, data):
        pos = None
        size = self.size
        for i in range(size):
            if self.list[i] == data:
                pos = i
                break
            
        return pos # index 반환
    
    def binary_search(self, data): # sorted list(오름차순)
        pos = None
        start = 0
        end = self.size - 1
        
        while(start <= end):
            mid = (start + end) // 2
            if data == self.list[mid]:
                return mid
            elif data > self.list[mid]:
                start = mid + 1
            elif data < self.list[mid]:
                end = mid - 1
            else:
                return pos
        
    def ternary_search(self, data): # sorted list(오름차순)
        pos = None
        start = 0
        end = self.size - 1
        
        while(start <= end):
            one_third = start + (end - start) // 3
            two_third = start + (end - start) * 2 // 3
            
            if data == self.list[one_third]:
                return one_third
            elif data == self.list[two_third]:
                return two_third
            elif data > self.list[two_third]:
                start = two_third + 1
            elif data < self.list[one_third]:
                end = one_third - 1
            elif data >= self.list[one_third] and data <= self.list[two_third]:
                start = one_third
                end = two_third
            else:
                return pos

if __name__ == "__main__":
    import random
    Data = [random.randint(1,100001) for _ in range(1,100001)]  # 십만개
    def Search_Test():
        print("원래 데이터: ")
        #print(Data, end="\n")
        print("찾기 테스트 시작 ")
        
        sort = Sort(True)
        start_time_sort = time.time()
        sorted = sort.quick_sort(Data)
        end_time_sort = time.time()
        search = Search(sorted) # search 객체
        
        print("10000번째 값 찾기: " + str(Data[10000]))
        print("순차검색: ")
        start_time = time.time()
        found_index = search.sequential_search(Data[10000])
        end_time = time.time()
        if found_index != None:
            print("%d" % sorted[found_index])
            print("%d마이크로초 걸립니다." % ((end_time - start_time) * (10**6)))
        else:
            print("값을 찾지 못했습니다.")
            
        print("이진검색: ")
        found_index = search.binary_search(Data[10000])
        if found_index != None:
            print("%d" % sorted[found_index])
            print("%d밀리 초 걸립니다." % ((end_time_sort - start_time_sort) * (10**3)))
        else:
            print("값을 찾지 못했습니다.")
            
        print("삼진검색: ")
        found_index = search.ternary_search(Data[10000])
        if found_index != None:
            print("%d" % sorted[found_index])
            print("%d밀리 초 걸립니다." % ((end_time_sort - start_time_sort) * (10**3)))
        else:
            print("값을 찾지 못했습니다.")
        
        print("정렬 테스트 이상 무")
    Search_Test()
    print("----------------------------------------")
