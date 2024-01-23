#Assignment no 03

#Question 1
num=1
num=int(input("Enter a number: "))

factorial=1

if (num>0):
    print("The factorial of 1 is 1")

else:
    print("The factorial of 0 is 0")


#Question 2
def fun(*a):
    sum=0
    for i in a:
        sum=sum+i
        print(sum)

sum(1,3,5,7,9,)


#Question 3
def fun(numerator):

if(%2==0):
    print("The quotient is 1")

else:
    print("The numerator is greater than 2")