"""
Name: Areeb Khan
Enrollment: 0103CS231080
Batch: 6
Batch Time: 12:10 to 13:50
"""

# Basic If-Else Problems:

"""
1. Write a program to check whether a number is positive, negative, or zero.
"""
num = int(input("Enter a number: "))
if (num == 0):
    print("Number is Zero.")
elif (num > 0):
    print("Number is Positive.")
else:
    print("Number is Negative")

""" OUTPUT
Enter a number: 5
Number is Positive.
"""

"""
2. Write a program to check whether a number is even or odd.
"""

num = int(input("Enter a number: "))
if (num%2 == 0):
    print("Number is even.")
else:
    print("Number is odd.")

""" OUTPUT
Enter a number: 9
Number is odd.
"""

"""
3. Write a program to check if a given year is a leap year or not.
"""

year = int(input("Enter year: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("Given year is Leap Year")
else:
    print("Given year is not Leap Year")

""" OUTPUT
Enter year: 2024
Given year is Leap Year
"""

"""
4. Write a program to find the greatest of two numbers.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if(num1 > num2):
    print("First number is greater.")
elif(num1 < num2):
    print("Second number is greater.")
else:
    print("Both are equal.")

""" OUTPUT
Enter first number: 5
Enter second number: 8
Second number is greater.
"""

"""
5. Write a program to check whether a person is eligible to vote (age >= 18).
"""

age = int(input("Enter age: "))
if(age>=18):
    print("You can vote.")
else:
    print("You cannot vote.")

""" OUTPUT
Enter age: 23
You can vote.
"""

"""
6. Write a program to check whether a given character is a vowel or consonant.
"""

character = input("Enter a character: ").lower()
if (character[0] in "aeiou"):
    print("Character is a vowel.")
elif (character[0] in "bcdfghjklmnpqrstvwxyz"):
    print("Character is a consonant.")

""" OUTPUT
Enter a character: a
Character is a vowel.
"""

"""
7. Write a program to check if a number is divisible by 5.
"""

num = int(input("Enter a number: "))
if (num%5 == 0):
    print("Number is divisible by 5.")
else:
    print("Number is not divisible by 5.")

""" OUTPUT
Enter a number: 50
Number is divisible by 5.
"""

"""
8. Write a program to determine whether a given number
is a single-digit, two-digit, or more than two-digitnumber.
"""

num = int(input("Enter a number: "))
length = len(str(num))
if (length == 1):
    print("Number is 1 digit.")
elif (length == 2):
    print("Number is 2 digits.")
elif (length > 2):
    print("Number is more than 2 digits.")

"""OUTPUT
Enter a number: 2234
Number is more than 2 digits.
"""

"""
9. Write a program to check whether a student has passed or failed (passing marks = 40).
"""

marks = int(input("Enter marks: "))
if(marks>=40):
    print("Student has passed the exam.")
else:
    print("Student has failed the exam.")

"""OUTPUT
Enter marks: 76
Student has passed the exam.
"""

"""
10. Write a program to find whether the entered number is a multiple of both 3 and 7.
"""

num = int(input("Enter a number: "))
if(num%3 == 0) and (num%7 == 0):
    print("Number is a multiple of both 3 and 7.")
else:
    print("Number is not a multiple of both 3 and 7.")

"""OUTPUT
Enter a number: 21
Number is a multiple of both 3 and 7.
"""

# Ladder If & Nested If:
"""
1. Write a program to find the greatest among three numbers.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("First Number is greater than Second Number is greater than Third Number.")
    else:
        print("First Number is greater than Third Number is greater than Second Number.")
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("Second Number is greater than First Number is greater than Third Number.")
    else:
        print("Second Number is greater than Third Number is greater than First Number.")
else:
    if num1 >= num2:
        print("Third Number is greater than First Number is greater than Second Number.")
    else:
        print("Third Number is greater than Second Number is greater than First Number.")

"""OUTPUT
Enter first number: 3
Enter second number: 7
Enter third number: 19
Third Number is greater than Second Number is greater than First Number.
"""

"""
2.Write a program to classify a person based on age:
Child (<13), Teenager (13-19), Adult (20-59), Senior (60+)
"""

age = int(input("Enter age: "))
if(age<13):
    print("Person is a child.")
elif(age >= 13 and age <=19):
    print("Person is a teenager.")
elif(age >= 20 and age <= 59):
    print("Person is a adult.")
elif(age >= 60):
    print("Person is a senior.")
else:
    print("Invalid age.")

"""OUTPUT
Enter age: 55
Person is a adult.
"""

"""
3. Write a program to assign grades based on marks:
90-100: A,
75-89: B,
50-74: C,
35-49: D,
<35: Fail.
"""

marks = int(input("Enter marks: "))
if(marks >= 90 and marks <= 100):
    print("Grade: A")
elif(marks >= 75 and marks <= 89):
    print("Grade: B")
elif(marks >= 50 and marks <= 74):
    print("Grade: C")
elif(marks >= 35 and marks <= 49):
    print("Grade: D")
elif(marks < 35 and marks > 0):
    print("Grade: Fail")
else:
    print("Invalid Marks")

"""OUPUT
Enter marks: 89
Grade: B
"""

"""
4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
"""

side1 = int(input("Enter side-1:"))
side2 = int(input("Enter side-2:"))
side3 = int(input("Enter side-3:"))
if(side1 == side2 == side3):
    print("Equilateral Triangle")
elif(side1 == side2 != side3) or (side1 != side2 == side3) or (side1 == side3 != side2):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

"""OUTPUT
Enter side-1:50
Enter side-2:50
Enter side-3:50
Equilateral Triangle
"""

"""
5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
"""

character = input("Enter a Character: ")
if character[0].isupper():
    print("Character is Uppercase.")
elif character[0].islower():
    print("Character is Lowercase.")
elif character[0].isdigit():
    print("Character is Digit.")
else:
    print("Character is Special Symbol.")

"""OUTPUT
Enter a Character: 6
Character is Digit.
"""

"""
6. Write a program to calculate electricity bill based on units:
Up to 100 units: ₹5 per unit,
101-200 units: ₹7 per unit,
Above 200 units: ₹10 per unit.
"""

unit = int(input("Enter units of elctricity used:"))
if(0 < unit <= 100):
    print("Cost:", unit*5)
elif(101 < unit <= 200):
    print("Cost:", unit*7)
elif(unit > 200):
    print("Cost:", unit*10)
else:
    print("Invalid input.")

"""OUTPUT
Enter units of elctricity used:174
Cost: 1218
"""

"""
7. Write a program to determine the largest of four numbers using nested if.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 >= num2:
    if num1 >= num3:
        if num1 >= num4:
            print("First number is largest.")
        else:
            print("Fourth number is largest.")
    else:
        if num3 >= num4:
            print("Third number is largest.")
        else:
            print("Fourth number is largest.")
else:
    if num2 >= num3:
        if num2 >= num4:
            print("Second number is largest.")
        else:
            print("Fourth number is largest.")
    else:
        if num3 >= num4:
            print("Third number is largest.")
        else:
            print("Fourth number is largest.")

""" OUTPUT
Enter first number: 50
Enter second number: 30
Enter third number: 22
Enter fourth number: 11
First number is largest.
"""

"""
8. Write a program to check if a given year is a century year and also a leap year
"""

year = int(input("Enter year: "))
if (year % 100 == 0):
    if (year % 400 == 0):
        print("Given year is a Century Year and also a Leap Year.")
    else:
        print("Given year is a Century Year but not a Leap Year.")
else:
    if (year % 4 == 0) and (year % 100 != 0):
        print("Given year is a Leap Year but not a Century Year.")
    else:
        print("Given year is neither a Century Year nor a Leap Year.")

""" OUTPUT
Enter year: 2200
Given year is a Century Year but not a Leap Year.
"""

"""
9. Write a program to classify BMI value:
Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).
"""

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)
if (bmi < 18.5):
    print("Underweight")
elif (18.5 <= bmi <= 24.9):
    print("Normal")
elif (25 < bmi <= 29.9):
    print("Overweight")
else:
    print("Obese")

"""OUTPUT
Enter year: 23
Given year is neither a Century Year nor a Leap Year.
"""

"""
10. Write a program to display the smallest number among three using nested if.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 <= num2):
    if (num1 <= num3):
        print("First number is the smallest.")
    else:
        print("Third number is the smallest.")
else:
    if (num2 <= num3):
        print("Second number is the smallest.")
    else:
        print("Third number is the smallest.")

"""OUTPUT
Enter first number: 30
Enter second number: 21
Enter third number: 175
Second number is the smallest.
"""

# For Loop Problems:

"""
1. Write a program using a for loop to print all Armstrong numbers between 100 and 999. 
(Armstrong number: sum of cubes of digits equals the number itself. Example: 153 => 1³+5³+3³ = 153).
"""

for num in range(100, 1000):
    temp = num
    digits = len(str(num))
    sum_of_powers = 0

    while (temp > 0):
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10
    if (sum_of_powers == num):
        print(num)

"""OUPUT
153
370
371
407
"""

"""
2. Write a program to generate and display the first n prime numbers using a for loop.
"""

n = int(input("ENter n: "))
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print(num)

"""OUTPUT
Enter n: 10
2
3
5
7
"""

"""
3. Write a program to display all numbers from 1 to 500 that are divisible by 3,
but the sum of their digits should not exceed 10.
"""

for num in range(501):
    if(num%3 == 0):
        temp = num
        sum_of_digits = 0

        while (temp > 0):
            digit = temp % 10
            sum_of_digits += digit
            temp //= 10
        if (sum_of_digits <= 10):
            print(num)

""" OUTPUT
0
3
6
9
12
15
18
21
24
27
30
33
36
42
45
51
54
60
63
72
81
90
102
105
108
111
114
117
120
123
126
132
135
141
144
150
153
162
171
180
201
204
207
210
213
216
222
225
231
234
240
243
252
261
270
300
303
306
312
315
321
324
330
333
342
351
360
402
405
411
414
420
423
432
441
450
"""

"""
4. Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:
        *
       ***
      *****
     *******
"""

n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

""" OUTPUT
Enter n: 5
    *
   ***
  *****
 *******
*********
"""

"""
5. Write a program to accept a string and check whether it is a pangram 
(contains all 26 alphabets at least once) using a for loop.
"""

string = input("Enter a string: ").lower()
is_pangram = True
for char in "abcdefghijklmnopqrstuvwxyz":
    if char not in string:
        is_pangram = False
        break
if is_pangram:
    print("The string is a Pangram.")
else:
    print("The string is not a Pangram.")

""" OUTPUT
Enter a string: The quick brown fox jumped over the lazy dog wvcghs
The string is a Pangram.
"""

"""
6. Write a program using a for loop to print all twin primes between 1 and 100.
(Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)).
"""

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
arr = []
for num in range(2, 101):
    if (is_prime(num)):
        arr.append(num)

for i in range(len(arr) - 1):
    if arr[i+1] - arr[i] == 2:
        print(arr[i], arr[i+1])

""" OUTPUT
3 5
5 7
11 13
17 19
29 31
41 43
59 61
71 73
"""

"""
7. Write a program that accepts a number from the user and prints whether it is a Harshad number (number
divisible by the sum of its digits) using a for loop
"""

num = input("Enter a number: ")
sum = 0
length = len(num)
for i in num:
    sum = sum + int(i)
if (int(num)%sum == 0):
    print("Given Number is Harshad Number.")
else:
    print("Given Number is not a Harshad Number.")

""" OUTPUT
Enter a number: 18                                                 
Given Number is Harshad Number.
"""

"""
8. Write a program to generate Pascal's Triangle up to n rows using a for loop.
"""

n = int(input("Enter value of n: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()

""" OUTPUT
Enter value of n: 5
    1 
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""

"""
9. Write a program using a for loop to display the sum of the series:
1² + 2² + 3² + ... + n²
"""

n = int(input("Enter value of n: "))
sum = 0
for i in range(1, n+1):
    sum += i**2
print("Sum of series:", sum)

"""OUTPUT
Enter value of n: 30
Sum of series: 9455
"""

"""
10. Write a program that accepts a number from the user and prints whether it is a Strong number (sum of
factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
"""

def factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return (num * factorial(num - 1))

num = int(input("Enter number: "))
temp = num
sum_of_factorial = 0

while (temp > 0):
    digit = temp % 10
    sum_of_factorial += factorial(digit)
    temp //= 10

if (sum_of_factorial == num):
    print("Given number is Strong number.")
else:
    print("Given number is not Strong number.")

""" OUTPUT
Enter number: 145
Given number is Strong number.
"""

# While loop

"""
1. Write a program using a while loop to find the reverse of a number and check if the reversed number is
prime. Example: Input = 73 → Reverse = 37 → Prime.
"""

num = int(input("Enter a number: "))

is_prime = True
if num <= 1:
    is_prime = False
elif num == 2:
    is_prime = True
else:
    rev_num, temp = "", str(num)
    length = len(temp) - 1
    
    while(length >= 0):
        rev_num = rev_num + temp[length]
        length -= 1
    rev_num = int(rev_num)
    i = 2
    while(i * i <= num):
        if(num % i == 0):
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{rev_num} is a Prime number.")
else:
    print(f"{rev_num} is not a prime number.")

""" OUTPUT
Enter a number: 127
721 is a Prime number.
"""

"""
2. Write a program that continues to accept numbers from the user until the sum of digits of all numbers
entered becomes greater than 100.
"""

num = 0
while(num <= 100):
    temp = int(input("Enter number: "))
    num += temp
print("Number exceeded 100")

""" OUTPUT
Enter number: 10
Enter number: 35
Enter number: 60
Number exceeded 100
"""

"""
3. Write a program using a while loop to check whether a number is a Duck number (a number containing zero
but not starting with zero, e.g., 202, 1203).
"""

num = int(input("Enter a number: "))
arr = list(str(num))
length = len(arr) - 1

is_duck = False
while(length > 0):
    if(arr[length] == '0'):
        is_duck = True
        break
    length -= 1

if(is_duck):
    print("The number is a duck number.")
else:
    print("The number is not a duck number.")

""" OUTPUT
Enter a number: 450
The number is a duck number.
"""

"""
4. Write a program using a while loop to accept a number and check if it is a Happy number. (A number is 
happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a 
happy number. 
"""

num = int(input("Enter a number: "))

visited = set()

while (num != 1 and num not in visited):
    visited.add(num)
    num = sum(int(digit) ** 2 for digit in str(num))

if(num == 1):
    print("Happy number.")
else:
    print("Not a Happy number.")

""" OUTPUT
Enter a number: 19
Happy number.
"""

"""
5.  Write a program using a while loop to find the largest prime factor of a given number.
"""

num = int(input("Enter Number: "))

factor = 2
while(factor * factor <= num):
    if(num % factor == 0):
        num //= factor
    else:
        if factor == 2:
            factor += 1
        else:
            factor += 2

print("Highest prime factor:", num)

""" OUTPUT
Enter Number: 750
Highest prime factor: 5
"""

"""
6. Write a program to repeatedly accept a string from the user until the string entered is a palindrome. 
"""

while(True):
    string = input("Enter string: ").lower()
    if(string == string[::-1]):
        break
print("String was palindrome. Exiting..")

"""OUTPUT
Enter string: musket
Enter string: keyboard
Enter string: mouse
Enter string: racecar
String was palindrome. Exiting..
"""

"""
 7. Write a program using a while loop to compute the sum of digits of a number until the result becomes a 
single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.
"""

num = int(input("Enter Number:"))

while(num >= 10): 
    sum_of_digits = 0
    while(num > 0):
        sum_of_digits += num%10
        num //= 10
    num = sum_of_digits

print("Number is:", num)

"""
Enter Number:9875
Number is: 2
"""

"""
8.  Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even 
=> n/2, if odd => 3n+1. Continue until n=1). 
"""

num = int(input("Enter Number: "))

print("Collatz Sequence")
while(num != 1):
    print(num, end=" ")
    if(num%2 == 0):
        num = num // 2
    else:
        num = 3 * num + 1
print(1)

"""OUTPUT
Collatz Sequence
23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1
"""

"""
9.  Write a program using a while loop to accept a number and check whether it is a Kaprekar number. 
(Kaprekar number: if square of the number can be split into two parts whose sum equals the number. 
Example: 45²=2025 => 20+25=45). 
"""

num = int(input("Enter a number: "))
square = num**2
digits = len(str(square))
is_kaprekar = False

i = 1
while i < digits + 1:
    right = square % (10 ** i)
    left = square // (10 ** i)

    if (left + right == num):
        is_kaprekar = True
        break
    i += 1

if is_kaprekar:
    print("Kaprekar number")
else:
    print("Not a Kaprekar number")

"""OUTPUT
Enter a number: 45
Kaprekar number
"""

"""
10. Write a program to simulate an ATM machine using a while loop where a user can:
• Check balance
• Deposit money
• Withdraw money (only if balance is sufficient)
• Exit
Continue until the user chooses to exit.
"""

balance = 1000

while True:
    print("-"*20)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = int(input("Select option(1-4): "))
    
    if(choice == 1):
        print("Your balance is:", balance)
    
    elif(choice == 2):
        amount = int(input("Enter amount to deposit: "))
        if(amount > 0):
            balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")
    
    elif(choice == 3):
        amount = int(input("Enter amount to withdraw: "))
        if(amount <= balance and amount > 0):
            balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")
    
    elif choice == 4:
        print("Exited.")
        break
    
    else:
        print("Try again.")

"""OUTPUT
--------------------
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Select option(1-4): 1
Your balance is: 1000
--------------------
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Select option(1-4): 2
Enter amount to deposit: 5000000
Deposited: 5000000
--------------------
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Select option(1-4): 3      
Enter amount to withdraw: 20000
Withdrawn: 20000
--------------------
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Select option(1-4): 4
Exited.
"""