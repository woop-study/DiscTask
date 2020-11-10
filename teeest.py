#10.43
n=int(input('не 1 введите натуральное число:'))
def summ(n):
    return n%10 +summ(n//10) if n>9 else n
print(summ(n))

a=0
def qwe(n):
    global a
    if n==0:
        return a
    else:
        a=a+1
        return qwe(n//10)
n=int(input())
print(qwe(n))

#10.46

l=0
def e(a,b,c):
    global l
    if c==0:
        return l
    else:
        a=a*b
        l=a
        return e(a,b,c-1)
a=int(input())
b=int(input())
c=int(input())
print(e(a,b,c))

l=0
def ew(a,b,c):
    global l
    if c==0:
        return l
    else:
        a=a*b
        l=a+l
        return ew(a,b,c-1)
a=int(input())
b=int(input())
c=int(input())
print(ew(a,b,c))

#10.49 erm

l=[123,234,345,45]
q=0
w=0
e=0
r=-1
def asd(n):
    global q
    global w
    global e
    global r
    if n!=[]:
        q=n[0]
        r+=1
        if q>e:
            w=r
            e=q
        del n[0]
        return asd(n)
    else:
        return w
print(asd(l))

