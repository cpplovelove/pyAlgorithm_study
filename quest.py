

def stringCheck():
    #list[::-1]하면 거꾸로됨!! 거꾸로랑 원문 같은지만 확인하면된다.
    n = int(input())
    for i in range(0,n):
        string= input()
        string=list(string.upper())
        flag=False #안맞는지
        while(len(string)!=1 and flag==False and len(string)!=0):
            if(string[0]==string[-1]):
                string=string[1:-1]
            else:
                print('NO')
                flag=True
        if(flag==False):
            print('YES')

def printOnlyNum():
    #숫자화시키는 방법 : res=res*10 + 새로운 숫자
    #isdigit함수로 숫자인지 찾기
    string= input()
    res,count =0,0
    for temp in string:
        if temp.isdigit()==True:
            res=res*10+int(temp)
    for i in range(1,res+1):
        if res%i==0:
            count+=1

    print(res)
    print(count)

def cardReversing():
    card_list=[]
    for i in range(1,21):
        card_list.append(i)
    print(card_list)
    for i in range(0,10):
        start,end= list(map(int,input().split()))
        tempList= card_list[start-1: end]
        card_list[start-1:end]=tempList[::-1]
        print(card_list)

def combindList():
    #그냥 더하고 sort호출하면 빠르게 해결되나 복잡도 증가, 퀵소트 이용!!
    #sort의 복잡도는 nlogn,이미 정렬된 리스트기때문에 잘하면 n번만에 가능하다
    indexA,indexB=0,0
    new_list=[]

    n = int(input())
    a_list = list(map(int, input().split()))
    n = int(input())
    b_list = list(map(int, input().split()))
    while(indexA!=len(a_list) and indexB!=len(b_list)):
        if(a_list[indexA]<=b_list[indexB]):
            new_list.append(a_list[indexA])
            indexA+=1
        else:
            new_list.append(b_list[indexB])
            indexB+=1
    while(indexA!=len(a_list)):
        new_list.append(a_list[indexA])
        indexA+=1
    while(indexB!=len(b_list)):
        new_list.append(b_list[indexB])
        indexB+=1
    print(new_list)

if __name__ == '__main__':
    #회문 문자열 검사
    # stringCheck()
    #숫자만 추출
    # printOnlyNum()
    #카드 역배치
    # cardReversing()
    #두 리스트 합치기
    # combindList()


    pass