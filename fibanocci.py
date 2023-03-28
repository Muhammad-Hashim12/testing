# 0 1 1 2 3 5 8 13 21 34 55.
i=int(input('enter the no: '))
a=0
b=1
e=[a,b]
while b<i:
    c=a+b
    e.append(c)
    a=b
    b=c
if i in e:
    print(f'{i} is fib')
else:
    print('is not fib')
    
   

    
    