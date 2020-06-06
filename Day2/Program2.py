num=int(input("Enter the number upto which you want to enter fibonacci series : "))
a=0
b=1
sum=0
count=1
while(count<num):
    print(sum,end = " ")
    count=count+1
    a=b
    b=sum
    sum=a+b
