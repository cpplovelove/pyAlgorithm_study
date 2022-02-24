#파이썬 입력받는 예제

def pythonIO():
    # a,b =input('숫자를 입력해주세요').split()
    a,b =map(int,input('숫자를 입력하세요 : ').split())
    # print(a+b)
    # print(a-b)
    # print(a*b)
    # print(a/b)
    # print(a//b) #몫 연산 5//3=1
    # print(a%b) #나머지 연산 5//3=2
    # print(a**b) #거듭제곱이라는 뜻
    a=4.3
    b=5
    c=a+b
    print(type(c))
    #형이 다른것끼리 연산시, 좀 더 넓은 범위의 형으로 합쳐진다

def forAndWhile():
    #입력한 숫자까지 홀수를 출력
    n=int(input())
    for i in range(1, n+1):
        if(i%2==1):
            print(i)

    #입력한 수까지의 합을 출력
    for i in range(1, n+1 ):
        sum+=i
    print('sum =', sum)
    #입력한 수의 약수를 출력
    for i in range(1, n+1):
        if n%i==0:
            print(i, end='  ') # 줄바꿈하지 않고 옆으로 출력

def charAndString():
    #대소문자, find/count, slice, char접근
    str="it is Time"
    print(str.upper())
    print(str.lower())
    print(str)

    temp = str.upper()
    print(temp.find('T')) #처음으로 발견된 인덱스번호를 출력
    print(temp.count('T')) #T의 갯수

    print(str)
    print(str[:2]) #slice기능 0번부터 2번까지 출력해준다
    print(str[3:5]) # 3-4번까지 출력한다
    print(len(str)) #길이를 출력

    for i in range(len(str)):
        print(str[i], end='  ')
    print()

    for char in str:
        print(char, end='*')
    print()

    for char in str:
        if char.isupper(): #대문자만 출력해주는 거임
            print(char)

    temp =66
    print(chr(temp)) #아스키 문자출력

import random as random
def listAndFunction():
    #리스트와 내장함수
    a= []
    b=list()

    a=[1,2,3,4,5]
    a.append(6) #마지막 인덱스에 값 삽입
    a.insert(3,7) #특정 인덱스에 값 삽입 3번에 7삼입
    a.pop(3) #3번에 있던 7이 사라짐
    a.remove(4) #변수로 들어온 값을 찾아서 삭제할 것
    print(a)
    print(a.index(5)) #해당인덱스에 들어있는 수를 출력
    print(sum(a))
    print(max(a), min(a))
    random.shuffle(a) #랜덤
    print(a)
    a.sort() #오름차순 정렬 출력
    print(a)
    a.sort(reverse=True) #내림차순 정렬 출력
    print(a)

    b=list(range(1,11))
    print(b)

    c=a+b
    print(c) #cat

def listAndFunction2():
    #리스트와 내장함수
    a=[23,12,36,53,19]
    print(a[:3]) #0-2
    print(a[1:4]) #1-3

    for x in a:
        if x%2==1:
            print(x,end=' ') #홀수번만 출력하도록 접근할 수 있음
    print()

    for x in enumerate(a):
    #튜플로 출력해주는데, x에 (0,23)과 같이 인덱스와 밸류를 출력해준다
    #리스트는 값 변경가능하나, tuple은 값 변경을 지원하지 않음 []리스트 ()튜플
       print(x)
       print(x[0], x[1], end='#')

    for index,value in enumerate(a):
        print(index, value)

    # if all(50>x for x in a): #a의 있는 변수 모두가 50보다크다면 yes
    if any(50>x for x in a): #하나라도 참이면 참
        print('yes')
    else:
        print('no')

def tdArray():
    # a=[0]*10 #0으로 초기화되는 1차원 리스트
    a=[[0]*3 for _ in range (3)] #3번반복하면서 1차원리스트를 만듬으로 3*3리스트 생성

    a[0][1],a[1][1]=1,2
    print(a)
    for x in a:
        #1차원리스트가 돼서 출력하게 된다
        #2차원리스트는 보통 이렇게 확인함
        print(x)

    for x in a:
        for y in x:
            #2차원리스트에 있는 요소 하나하나 출력하게 된다 2중포문
            print( y)

#익명함수, 람다표현식 = 변수에 할당해서 사용해야함
plus_two = lambda  x: x+2
print_djd= lambda  x: x%2==0
print(plus_two(2))

a=[1,2,3]
print(list(map(plus_two,a))) #맵은 인자가 두개여서, 내장함수, 리스트들어가면 함수랑 매핑시킴
print(list(map(print_djd,a)))
print(list(map(lambda  x: x+1, a))) #따로 선언하지 않아도 이렇게 선언가능하다, 코드 간단히 사용가능

#보통 sort할때 사용마니 한다

if __name__ == '__main__':
    # forAndWhile();
    # charAndString();
    # listAndFunction2();
    # tdArray()
    pass