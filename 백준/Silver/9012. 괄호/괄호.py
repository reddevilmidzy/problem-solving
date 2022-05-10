import sys
input = sys.stdin.readline

for i in range(int(input())):
    stk = [] # 괄호 담을 스택
    ans = "YES" # 대답 설정
    for f in input().rstrip(): # 인풋 낱개 하나하나
        if f == "(":
            stk.append(f) # 하나씩 담기
        else:
            if len(stk) > 0:
                stk.pop() # )가 입력된는 상황이다. 만약 (가 있다면 (를 뺀다
            else:
                ans = "NO" # )가 입력될때 (가 없다면 대답은 노
    if len(stk) > 0:
        ans = "NO" # 최종적으로 봤을때 남아있는 ( ) 둘 중 하나라도 남아있다면 노
    
    print(ans)