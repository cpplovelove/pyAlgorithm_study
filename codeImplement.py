

def kth_divisor_number():
    #어떤 자연수 p, q가 있을때 나눠서 0이면 q는 p의 약수이다
    #두개의 자연수가 주어졌을때 N개의 약수중 K번째로 작은수를 출력하는 프로그램
    n,k = map(int,input().split())
    list=[]
    for i in range(1,n+1):
        if(n%i==0):
            list.append(i)
    list.sort()
    print(list[k-1])

def kth_number():
    #n개의 숫자로 이뤄진 숫자열이 주어지면, 해당 숫자열 중 s번째부터 e까지 오름차순 했을때 k번째 숫자
    n,s,e,k = map(int, input().split())
    temp_list= list(map(int,input().split()))
    temp_list=temp_list[s-1:e]
    temp_list.sort()
    print(temp_list[k-1])

def kth_max_number(): #**
    #자연수 n,k를 입력받아서 3장뽑아서 더한값중 k번째 큰 값
    n, k= map(int, input().split())
    a=list(map(int,input().split()))
    #중복을 제거하기 위해서 set사용

    res= set()#3개를 선택해서 res에 추가
    for i in range(n):
        for j in range(i+1,n):
            for m in range(j+1,n):
                temp=a[i]+a[j]+a[m]
                res.add(temp)
    res= list(res)
    res.sort(reverse=True)
    print(res[k-1])

#최솟값 그냥 쭉 보면서 구하기 예제
# arr = [5,4,3,2,3,23,4,1,-2]
# arrMin=float('inf')
# for i in range(len(arr)):
#     if arr[i]<arrMin:
#         arrMin=arr[i]
# print('최솟값',arrMin)

def refValue():
    #대표값 구하기 n명이 주어질때 평균을 구하고, 평균에 가장 가까운 넘이 몇번째인지 출력
    #답이 2개일 경우 성적이 높은 넘의 번호 출력, 여러개일 경우 번호가 빠른넘이 답
    n = int(input())
    score_list= list(map(int, input().split()))
    avg = round(sum(score_list)/n)
    print(avg)
    print(score_list[10:22])

    temp_list=list(map(lambda x:abs(x-avg),score_list))
    #차이가 가장 작은 수, 차이가 같은 경우 앞에있는거 출력

    print(temp_list[10:22])
    print(temp_list.index(min(temp_list))+1)
    #파이썬에서는 round함수가 round_half_even방식을 택한다.
    #a = 4.5000 -> print(roud(a)) 이렇게 정확한 하프지점에서는 짝수쪽으로 간다
    #논리적 오류가 생길 수 있기 때문에 66.5는 67이돼야하는데 66이 되니까 round대신 소숫점자리가 0.5일 경우 0.5를 더해주고 int형변환해준다.!!!

def dice(): #**
    #정다면체 문제 : 두개의 n,m면체의 주사위를 던져서 나올 수 있는 눈의 합중 가장 확률이 높은 숫자를 출력
    n,m = map(int, input().split())
    list=[]
    bucket=[0]*100
    #1부터 더하는 모든 경우를 구하는 거기 때문에 i+1이딴식으로 돌리면 안됨!!
    for i in range (1,n+1):
        for j in range(1, m+1):
            if i+j in list:
                bucket[i+j]+=1
            list.append(i+j)

    for i in range(len(bucket)):
        if bucket[i]==max(bucket):
            print(i,end=' ')

def sum_number():
    #첫줄에 자연수가 주어지고 n개의 자연수가 주어진다. 각 자연수는 10,000,000을 넘지 않는다
    n= int(input())
    number_list=list(map(int,input().split()))
    sum_list=[]

    for number in number_list:
        sum=0
        while number>1:
            temp=int(number%10)
            sum+=temp
            number=number/10
        sum_list.append(sum)

    print(number_list[sum_list.index(max(sum_list))])

def eraera(): #**
    #에라토스테네스 체
    #1-n까지 수 중 소수의 개수를 가장 빨리 구하는 방법
    n = int(input())
    ch=[0]*(n+1)
    cnt=0 #소수의 갯수

    for i in range(2,n+1):
        if( ch[i]==0):
            cnt+=1
            for j in range(i,n+1,i): #i를 배수로
                ch[j]=1
    print(cnt)

#뒤집은 소수
def reverse(x):
    cnt, reverseNumber=0,0
    list= []
    while(x>=1):#자릿수 구하기
        temp= int(x%10)
        list.append(temp)
        x/=10
    while len(list)!=0:
        reverseNumber+=list.pop()*pow(10,cnt)
        cnt+=1
    return reverseNumber

def reverse2(x):
    res=0
    while x>0:
        temp=x%10
        res=res*10+temp
        x=x//10
    return res

def isPrime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def isPrime2(x):
    if x==1:
        return False
    for i in range(2, x//2+1):#절반만 돌아도 나머지는 2배니까 반만돌고 판별가능
        if x%i==0:
            return False
    else:
        return True

def score():
    #점수계싼문제
    n=int(input())
    mon_list= list(map( int, input().split()))
    continuity=0
    score=0
    for i in mon_list:
        if(i==1):
            continuity+=1
            score+=continuity
        else:
            continuity=0
    print(score)

if __name__ == '__main__':
    #k번째 약수
    # kth_divisor_number()
    #k번째 수
    # n = int(input())
    # for i in range(n):
    #     kth_number()
    #k 번째 큰 수
    # kth_max_number()
    #대표값
    # refValue()
    #정다면체
    # dice()
    #자릿수의 합
    # sum_number()
    #max=-2147000000
    #에라토스테네스 체
    # eraera()

    # #뒤집은 소수
    # n = int(input())
    # list = list(map(int, input().split()))
    # answer=[]
    # for number in list:
    #     revNum = reverse(number)
    #     if(revNum==1):
    #         continue
    #     if (isPrime(revNum)==True):
    #         print(revNum,end=' ')

    #제일 조은 조건이 ifelse문의 맨 처음으로 와야한다

    score()
    pass