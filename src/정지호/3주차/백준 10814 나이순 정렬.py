import sys
input = sys.stdin.readline

N = int(input())
li = [] # 입력 받은 문자열을 공백 기준으로 쪼개어 만든 리스트를 받는 리스트
li_1 = [] # 입력 받은 문자열의 정수 부분과 인덱스로 이루어진 리스트를 받는 리스트
li_2 = [] # 회원들 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순으로 정렬된 리스트들을 가지는 리스트


for i in range(N): # N번만큼 반복(i는 0 ~ N-1)
    li.append(input().split())
    li_1.append([int(li[i][0]), i])

result = sorted(li_1, key = lambda x : (x[0], x[1]))
# key: 정렬 기준을 정해줄 수 있는 파라미터
# lambda 인자(매개변수) : 표현식(인자를 이용한 동작) => 일반함수를 가볍게 만든 함수라고 생각하자. ex) lambda x:x*2 
# => 회원들 나이를 오름차순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순으로 정렬

for i in range(N):
    li_2.append([str(result[i][0]), li[result[i][1]][1]]) # join을 써주기 위해 회원의 나이를 str()로 감싸준다.
    print(" ".join(li_2[i])) # " " 을 기준으로 정수와 회원이름을 합쳐준다. 