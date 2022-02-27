

def getMaxGrid():
    #격자판
    n = int(input())
    a=[list(map(int,input().split())) for _ in range(n)]

    row_max, col_max, dae_max= 0,0,0
    row,col,daex,daey= 0,0,0,0
    for i in range (0,n):
        daex+=a[i][i]
        daey+=a[n-i-1][n-i-1]
        for j in range(0,n):
             row+=a[i][j] #가로 부분의 합
             col+=a[j][i] #세로 부분의 합
        if(row_max<row):
            row_max=row
        if(col_max<col):
            col_max=col
        row,col=0,0
    print(max(daex,daey,col_max,row_max))

def appleTree():
    n= int(input())
    a=[list(map(int, input().split())) for _ in range(n)]
    res=0
    s=e=n//2
    for i in range(n):
        for j in range(s, e+1): #s부터 e 까지
            res+=a[i][j]
        if i<n//2:
            s-=1
            e+=1
        else:
            s+=1
            e-=1
    print(res)
    pass

def comingSoon():
    n = int(input())
    a=[list(map(int, input().split())) for _ in range(n)]
    m= int(input())
    for i in range(m):
        h, t, k = map(int,input().split())
        if t==0:
            for _ in range(k):
                a[h-1].append(a[h-1].pop(0)) #왼쪽으로 회전, 맨앞에껄 뒤로
        else:
            for _ in range(k):
                a[h-1].insert(0, a[h-1].pop()) #오른쪽으로 회전, 끝에껄빼서 처음으로

    res=0
    s,e=0,n-1
    for i in range(n):
        for j in range(s,e+1):
            res+=a[i][j]
        if(i<n//2):
            s+=1
            e-=1
        else:
            s-=1
            e+=1
    print(res)






    pass

def bongbong():
    n=int(input())
    a=[list(map(int,input().split())) for _ in range(n)]
    a.insert(0, [0]*n)
    a.append( [0]*n)
    for x in a:
        x.insert(0,0)
        x.append(0)

    count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(a[i][j]!=0):
                #dx=-1,0,1,0
                #dy=0,1,0,-1
                # if all(a[i][j]> a[i+dx[k]] for k in range (4)):
                if(a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1]):
                    count+=1
    print (count)

def sudoku():
    #행, 열, 구간을 체크하기 위한 행렬을 만들것
    a = [list(map(int,input().split())) for _ in range (9)]

    for i in range(9): #행렬체크
        rowCheck = colCheck  = [0] * 10
        for j in range(9):
            rowCheck[a[i][j]]=1
            colCheck[a[j][i]]=1
        if(sum(rowCheck)!=9):
            print("No")
            return

    for i in range(3):#그룹체크
        for j in range(3):
            squCheck=[0]*10
            for k in range(3):
                for s in range(3):
                    squCheck[a[i*3+k][j*3+s]]=1
            if(sum(squCheck)!=9):
                print('No')
                return

    print('Yes')
    pass

def loopString():
    a = [list(map(int,input().split())) for _ in range(7)]
    cnt =0
    for i in range(3):
        for j in range(7):
            temp=a[j][i:i+5]
            if temp==temp[::-1]:
                cnt+=1
            for k in range(2):
                if a[i+k][j]!=a[i+5-k-i][j]:
                    break
            else:
                cnt+=1
    print(cnt)
    pass

if __name__ == '__main__':
    #격자판 합 출력
    # getMaxGrid()
    #사과나무( 다이아몬드)
    # appleTree()
    #곳감(모래시계)
    # comingSoon()
    #봉우리
    # bongbong()
    #스도쿠
    sudoku()
    pass