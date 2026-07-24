def solution(s):
    result=[]
    for i in range (0,len(s),2):
        pairs= s[i:i+2]
        if len(pairs)==2:
            pass
        else:
            pairs=pairs+"_"
        result.append(pairs)
            
    return result
            
        
x= solution("abcdefg")
print(x)
