dic = {}
#dicSize = int(input()) 
color = list(input().split())
currentMaxSize = 0
startIndex = 0
result = True
# 7
# 3 1 4 1 5 9 2 


while result:
    fail = 0
 
    for i, num in enumerate(color[startIndex:]): 
      if num not in dic:  # 공통되지 않는다면
        dic[num] = i
        print(dic)
      else: # 공통된다면
        if currentMaxSize < len(dic):
            currentMaxSize = len(dic)  # 공통되기 전까지의 사이즈
        startIndex = dic[num] + 1 # 공통된 수의 다음 인덱스 부터 시작하기 위한 처리
        dic = {} # 딕셔너리 초기화
        fail = 1 # 공통된 걸 겪었는지 확인하기 위한 변수
        break
    
    


    if fail != 1:
      if currentMaxSize < len(dic):
            currentMaxSize = len(dic)
      print(currentMaxSize)
      result = False
      