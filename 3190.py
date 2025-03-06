#정사각형 게임 보드 칸 수 입력받기
matrixNum = int(input())

#게임 보드 만들기
martix = [([0]*matrixNum) for _ in range(matrixNum)]

#사과의 갯수 입력받기
appleNum = int(input())

for _ in range(appleNum):
    appleRow, appleCol = map(int, input().split())
    
    

