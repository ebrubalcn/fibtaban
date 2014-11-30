list=[1,1]
def fibo(c):
    i=1
    while i<c-1:
        b=list[i]+list[i-1]
        list.append(b)
        i+=1
def ikili_taban(n):
    a=str(n)
    d=len(a)
    fibo(d)
    i=0
    sonuc=0
    while i<d:
        if a[i]=='1':
            sonuc +=list[i]
            i+=1
        else:
            i+=1
    print sonuc
