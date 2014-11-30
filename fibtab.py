def fibonacci(n):
    list=[1,1]
    i=0
    while list[i]<=n:
        a=list[i]+list[i+1]
        if a<=n:
            list.append(a)
            i+=1
        else:
            break
    i=-1
    while n>=0 and i>=(-1*len(list)):
        if n>=list[i]:
            n=n-list[i]
            list[i]=1
            i-=1
        else:
            list[i]=0
            i-=1
    print list
    
