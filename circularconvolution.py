def cyclicdelay(x,m):
    N=len(x); y=[]
    for n in range(0,N):
        if n-m >= 0:
            idx=(n-m) % N
        else:
            idx=N+(n-m)
        y.append(x[idx])
    return y
x=[1,2,3,4,5,6]
m=5
print(cyclicdelay(x,m))