# given a sorted array Arr of size N and a number X , 
# you need to find the number of occurancee of X in Arr.
#example 1:
#Input:n=7,X=2
# Arr[]={1,1,2,2,2,2,3\

n=int(input("enter the no of values : "))
x=int(input("enter the value to be searched : "))
print("enter the values : ")
arr=[]
count=0
for i in range(n):
    a=int(input())
    arr.append(a)
    if a==x:
        count=count+1
print(arr)    
print(count)
        
        