print('Program to Sum all the numbers given by user')
number=[]
n=int(input('Enter no of times you want to enter number? '))
for i in range(n):
    n1=int(input('Enter number here = '))
    number.append(n1)
print('your input number list is' ,number)
print('your sum of number is' , sum(number))
