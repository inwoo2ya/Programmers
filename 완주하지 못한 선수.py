def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    #같은 배열끼리 묶어준다
    for a,b in zip(participant,completion):
        if a != b :
            return a

    return participant.pop()
