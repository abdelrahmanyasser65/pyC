def maxNumber(num1,num2,num3):
    maxNum=num1
    if num2>maxNum:
        maxNum=num2
    if num3>maxNum:
        maxNum=num3
    return maxNum

num1=int(input("Enter the first Number : "))
num2=int(input("Enter the second Number : "))
num3=int(input("Enter the third Number : "))
maxNum=maxNumber(num1=num1,num2=num2,num3=num3)
print("The max Number is : ",maxNum)
