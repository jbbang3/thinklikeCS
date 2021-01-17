#Ch7 Exercises
# Q1=============================================================
# import math

# def test_square_root(a):
#     x=a/5
#     while True: 
#         y=(x+a/x)/2
#         if abs(y-x)<0.000001:
#             return y
#             break
#         x=y


# print('{:<5s}{:<15s}{:<15s}{:<12s}'.format('a','mysqrt(a)','math.sqrt(a)','diff'))
# print('{:<5s}{:<15s}{:<15s}{:<12s}'.format('-','---------','-----------','----'))

# for a in range(8):
#     my=test_square_root(a+1)
#     existing=math.sqrt(a+1)
#     #print (str(float(a+1))+"  "+ str(my)+"   "+str(existing)+"   "+str(abs(my-existing)))  
#     print('{:<5.1f}{:<15.8f}{:<15.8f}{:<12.8f}'.format(float(a+1),my,existing,abs(my-existing)))



 # Q2===========================================================

# import math
# def eval_loop():
#     while True:
#         if x=="done":
#            break
#         x=input('>')
#         y=eval(x)
#         print(y)

# eval_loop()

# Q3===========================================================

import math



def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)



def estimate_pi():
    k=0
    newx=0
    while True:
        c=2*math.sqrt(2)/9801
        top=factorial(4*k)*(1103+26390*k)
        bottom=((factorial(k))**4)*396**(4*k)
        new=c*top/bottom
        newx=newx+new
        k=k+1
        if new<1e-15:
            break
        
    return newx 

value=estimate_pi()
print(1/value)
print(str(math.pi))