from collections import deque
def apply(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="x":
        return a*b
    elif c=="/":
        return a/b
def tree(arr: list):
    if not arr:
        return
    q=[]
    for c in arr:
        if isinstance(c, (int,float)):
            q.append(c)
        else:
            a=q.pop()
            b=q.pop()
            d=apply(a,b,c)
            q.append(d)   
    return round(q[0],2)
print(tree([3,4,"+",2,"-",6,"/"]))
