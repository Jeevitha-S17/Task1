1.Sum of Two numbers
a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
c = a+b
print('Sum of two numbers is",c)
Ouput:
Enter num1:5
Enter num2:2
Sum of two numbers is 7

2.Odd or even checker
a = int(input("Enter a number"))
if a%2==0:
   print(a,"is a even number")
else:
   print(a,"is a odd number")
Output:
Enter a number 3
3 is a odd number

3.Factorial Calculation
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
Output:
Enter a number:3
The factorial of 3 is 6

4.Fibonacci Series
n = int(input("Enter a num"))
a = 0
b = 1
next = b  
count = 1
while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()
Output:
Enter a num 3
1 2 3

5.String Reverse 
s = input("Enter a string: ")
rev = s[::-1]
print("Reversed string:", rev)
Output:
Enter a string:hello
Reversed string:olleh

6.Palindrome Check
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
Output:
Enter a string:nitin
Palindrome

7.Leap Year Check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
Output:
Enter a year:2026
Not a Leap Year

8.Armstrong Number
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
Output:
Enter a number:153
Armstrong Number



