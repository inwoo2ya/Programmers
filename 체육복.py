def solution(n, lost, reserve):
    answer = 0
    s_lost = set(lost)-set(reserve)
    s_reserve = set(reserve)-set(lost) # 같은 거 삭제
    for i in s_reserve: #현재 가지고 있는 사람을 센다.
        if i-1 in s_lost: #잃어버린사람중 가지고있는사람의 왼쪽에 사람이 있나 확인
            s_lost.remove(i-1)
        elif i+1 in s_lost:#잃어버린사람들중 가지고있는 사람의 오른쪽에 사람이 있나 확인
            s_lost.remove(i+1)
    print(s_lost)
    print(s_reserve)
    answer = n-len(s_lost) # 결국 체육복을 빌린사람의 수 계산
    return answer
