def solution(numbers, hand):
    result=[]
    keypad ={1:[0,0],2:[1,0],3:[2,0],
           4:[0,1],5:[1,1],6:[2,1],
           7:[0,2],8:[1,2],9:[2,2],
           '*':[0,3],0:[1,3],'#':[2,3]}
    answer=''
    r=keypad['#']
    l=keypad['*']
    for i in numbers :
        n = keypad[i]
        if i in [1,4,7]:
            result.append('L')
            l = n
        elif i in [3,6,9]:
            result.append('R')
            r = n
        else : 
            rd = 0
            ld = 0
            for a,b,c in zip(l,r,n):
                rd +=abs(b-c)
                ld +=abs(a-c)
                
            if rd > ld :
                result.append('L')
                l=n
            elif ld > rd :
                result.append('R')
                r= n
            
            else:
                if hand=="right":
                    result.append('R')
                    r=n
                elif hand =="left":
                    result.append('L')
                    l=n
    for i in result :
        answer+=i
    return answer
