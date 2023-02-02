#!/usr/bin/env python
# coding: utf-8

# Write a Python Program to Find the Factorial of a Number?
# 

# In[2]:


i=int(input("Enter a number"))
fact=1
while(i>0):
    fact=fact*i
    i=i-1
    
print(fact)
    


# In[ ]:





# Write a Python Program to Display the multiplication Table?
# 

# In[4]:



num = int(input("Display multiplication table of? "))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# In[ ]:





# Write a Python Program to Print the Fibonacci sequence?
# 

# In[8]:


num=int(input("Enter the length of fibonacci"))

def fib(n):
    if(n==0):
        return 0
    if(n==1 ):
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(0,num):
    print(fib(i))
    


# Write a Python Program to Check Armstrong Number?
# 

# In[41]:


num_string=input("enter the number")
digits=len(num_string)
num=int(num_string)
numlist=[]
n=10
while(num!=0):
    numlist.append(num%n)
    num=int(num/10)
    
sum1=0   

for i in range(0 ,digits):
    x=len(numlist)
    ##print(pow(numlist[i],digits))
    sum1=sum1+(pow(numlist[i],digits))
    
if(int(sum1)==int(num_string)):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'Interval')


# In[50]:


def armstrong(num):
    original=num
    digits=0    
    numlist=[]
    n=10
    while(num!=0):
        numlist.append(num%n)
        num=int(num/10)
        digits=digits+1

    sum1=0   

    for i in range(0 ,digits):
        x=len(numlist)
        ##print(pow(numlist[i],digits))
        sum1=sum1+(pow(numlist[i],digits))

    if(sum1==original):
        print(int(original))
        
x=int(input("Enter the start"))
y=int(input("Enter the end"))

for i in range(x,y):
    armstrong(i)
    


# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'Numbers')


# In[57]:


i=int(input("Enter the number"))
sum=0
while(i!=0):
    sum=sum+i
    i=i-1
print("sum is :",sum)


# In[ ]:





# In[ ]:




