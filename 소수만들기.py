from itertools import combinations #중복을 허용하지 않고, 순서 의미가 있는 조합을 리턴해준다.

def isprime(num) : #에라토스테네스의 체 소수 판별 알고리즘 함수
    if num == 1 :
        return False
    else :
        for i in range(2, int(num**0.5)+1): #이건 아직도 모르겠다.......
            if num % i == 0 : # i로 나누었을때 나누어지면 소수가 아니다.
                return False
        return True # 나눠지지 않으니 소수 이다.

def solution(nums):
    answer = 0
    comb = list(combinations(nums,3))#nums 배열을 3개씩 조합 후 list 변경
    for n in comb :
        if isprime(sum(n)):
            answer += 1

    return answer
