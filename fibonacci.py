#Num= raw_input( 'enter a number:' )
Num = 4
n1=0
n2=1
count=0
if Num <= 0 :
    print("Please enter a positive number")
elif Num == 1 :
    print("The fibonacci series is :", Num)
else :
    print("The Fibonacci sequence for " , Num ,"is ")
    while count<Num :
        print (n1,end='')
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1
