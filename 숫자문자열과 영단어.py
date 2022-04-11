s = (input())

dict ={}
en =['zero','one','two','three','four','five','six','seven','eight','nine']
for i in range(10):
    dict[en[i]]=i

    result =''
    eng=''
    for i in s:
        if i.isdigit(): #숫자 확인
            result=result+i
        elif i.isalpha(): #문자 확인
            eng=eng+i 
            if eng in dict.keys() : #이어붙이다가 숫자단어가 되면
                result = result+str(dict[eng]) #dict에서 찾아서 치환
                eng =''#초기화
print(int(result))
