def solution(arr):
    result = [arr[0]]
    for i in range(1,len(arr)):
        if result[len(result)-1] == arr[i] :
            continue
        result.append(arr[i])

    return result
