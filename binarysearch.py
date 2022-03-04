

def binarySearch():
    # 이분탐색
    n,m=map(int,input().split())
    templist= list(map(int,input().split()))
    templist.sort()
    lt,rt= 0, n-1

    while (lt<=rt):
        mid = (lt + rt) // 2
        if(templist[mid]==m):
            print(mid+1) #index출력
            break
        elif (templist[mid]>m):
            rt=mid-1
        else:
            lt=mid+1

def main():
     

if __name__ == '__main__':
    main()