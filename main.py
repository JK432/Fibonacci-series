# Write a Python program to display the Fibonacci sequence for n terms
x=int(input())
first=0
second=1
print(first)
print(second)
i=0
while(i<x-2):
    third=first+second
    print(third)
    first=second
    second=third
    i=i+1
 
