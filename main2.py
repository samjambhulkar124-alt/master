# print("this 1234 !@#$$ is new class")
# This is an new class
# a = "hello world"
# print(a)
# print(a[0::2])


# age = int(input("what is your age "))
# if age >=25:24
#     print("your age is similor to my age")
# else:
#     print("you are yonger than me")

# a = "A"

# print(ord(a))

# b = 65
# print(chr(b))

# a = "hello Brother"
# print(a[0:5:])

# a = 12
# a = str(a)

# print(type(a))

# a = "12"
# a = int(a)

# print(type(a))

# a = 0
# print(bool(a))

# print(12/3)

# name = "sumit"
# age = 30

# # print("hello my name is", name,"and my age is",age)
# print(f"my name is {name} and my age is {age}")

# age = int(input("hello what is your age "))
# print(age)

# name = (input("enter your name:-"))
# age = int(input("enter your age:-"))
# print(f"hello my name is {name} and my age is {age}")

# a = 5
# b = 32

# print(a + b)
# print(b - a)
# print(a * b)
# print(b / a)
# print(b // a)
# print(5**2)
# print(5**100)
# print(32%5)

# a = 20
# a = a + 20
# a = a + 40
# a = a + 60

# print(a)

# a = 20
# a +=20
# a +=40
# a +=60
# a /=2

# print(a)

# a = 12.1
# b = 12
# print(a == b)
# print(a != b)
# print(a > b)

# print(12<13 and 13==13)
# print(not 13>12)

# IF Statement
# num = int(input("Enter the number:-"))
# if num >= 10:
#     print("number is grether than 10")
# else:
#     print("the number is less than 10") 

# mark = int(input("enter the number:-"))
# if mark >= 87:
#     print("Gread A")
# elif mark>= 70:
#     print("Gread B")
# elif mark>= 55:
#     print("Gread C")
# elif mark >=45:
#     print("Gread D")
# else:
#     print("Fail")

# G = input("Enter the your gender:-male or Female ")

# if G == "Male" or G =="male" or G=="m" or G=="M":
#     print("Good Morning Sir")
# elif G == "female" or G=="Female" or G=="F" or G=="f":
#     print("Good Morning Maam")
# else:
#     print("invalid Gender")

# G = input("Enter the your gender:-male or Female ")

# if G in ["male", "Male", "m", "M"]:
#     print("Good Morning Sir")
# elif G in  ["female", "Female", "F", "f"]:
#     print("Good Morning Maam")
# else:
#     print("invalid Gender")

# num = int(input("Enter the number :- "))
# if num %2 == 0:
#     print("This is Even number")
# else:
#     print("This is Odd number")

# name = input("Enter Your Name:-")
# age = int(input("Enter your age:-"))

# if age >= 18:
#     print(f"Hello{name} you are eligible for votting")
# else:
#     print(f"Hello {name} apply first for vooting card")

# t = int(input("please enter Temprature:-"))
# if t < 0:
#     print("Freezing cold")
# elif t >=0 and t < 10:
#     print("Verry cold")
# elif t >=10 and t < 20:
#     print("cold")
# elif t >=20 and t < 30:
#     print("plasent")
# elif t >=30 and t < 40:
#     print("hot")
# else: 
#     print("temrature is verry hot")

# FOR LOOP
# a = range(1,21,2)
# for i in a:
#     print(i)

# for i in range(3,16,3):
#     print(i)

# Defoult value
# for i in range(5):
#     print(i)

# Reverce range
# for i in range(20,1,-2):
#     print(i)

# for i in range(5,51,5):
#     print(i)

# write a table
# n = int(input("Enter ther the number for table:- "))
# for n in range(n,n*10+1,n):
#     print(n)

# a = "jambhulkarsumitj"
# for i in range (10):
#     print(a[i])

# a = "sumit sunil jambhulkar"
# print(len(a))
# for i in range (len(a)):
#     print(a[i])  

# a = "pytho"
# for i in a:
#     print(i)

# for i in range(1,20):
#     if i == 15:
#         break
#     else:
#         print(i)

# for i in range(1,20):
#     if i == 15:
#         break
#     print(i)

# for i in range(1,20):
#     if i == 15:
#         continue
#     print(i)

# n = int(input("enter the number"))
# for i in range(n):
#     print("hello word")

# n = int(input("enter number "))
# for i in range(1,n+1):
#     print(i)

# n = int(input("enter the number"))
# for i in range(n,0,-1):
#     if n == 5:
#         break
#     print(i)

# n = int(input("which table you want"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# n = int(input("enter the number:- "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
#     print(f"the sum number is {sum}")

# n = int(input("enter the number:- "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
#     print(f"the sum number is {fact}")

# n = int(input("enter the number:- "))
# even = 0
# odd = 0
# for i in range (1 ,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"sum of even number:-{even} and sum of odd number:-{odd}")

# l = [12,16,12,19,17]
# largest = l[0]
# second = l[0]
# for i in l:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second:
#         second = i
# print(second, largest)

# a = [1,2,4,4,5,6]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("list not sorted")
#         break
# else:
#     print("list is sorted")


# write hello world 100 time with help of loop
# a = "Hello World"
# for i in range(100):
#     print(a)

#write a loop in reverse order
# a = "hello world"
# for i in range(len(a),0,-1):
#     print(a)


#print a table
# table = int(input("witch table you want:- "))
# for i in range(table,table*10+1,table):
#     print(i)

#write a loop in reverse order
# a = "hello world"
# for i in range(len(a),0,-1):
#     print(a)

# a= int(input("enter first number"))
# b= int(input("enter Second number"))
# if a > b:
#     print(f"number {a} is Greater Than {b}")
# else:
#     print(f"number {b} is greter than {a}")

# name= input("enter your name:- ")
# gender= input("enter your gender hear:- ")
# male = "mr."
# female = "mrs."
# if gender == male:
#     print(f"hello {male}{name}")
# else:
#     print(f"hello {female}{name}")

# num = int(input("enter the number:- "))
# if num%2==0:
#     print("even number")
# else:
#     print("odd Number")

# name = input("enter your name:- ")
# age = int(input("Enter your age:- "))
# if age >=18:
#     voter_id = input("you have voter id?")
#     if voter_id == "yes":
#         print(f"Hello {name} you are eligible for votting")
#     else:
#         print(f"hello {name}, apply for votting id first")
# elif age <= 18:
#     print(f"hello {name} you eligible for votting after {18 - age}")
# else:
#     print("Please provide correct input") 

# year = int(input("enter the year"))
# if year%100==0 and year%400==0:
#     print(f"{year} is a leap year")
# elif year%100!=0 and year%4==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} not a leap year")

# FOR LOOP
# a = range(2,21,2)
# for i in a:
#     print(i)

# for i in range(1,5):
#     print(i,end=" ")

# marks = int(input("enter your marks:- "))
# if marks >=80 and marks == 100:
#     print("Grade A")
# elif marks >=70 and marks <80:
#     print("Grade B")
# elif marks >= 60 and marks <70:
#     print("Grad C")
# elif marks >=45 and marks <60:
#     print("Grad D")
# else:
#     ("pass")

# rohit = 12*3
# print(rohit)


'''  FOR LOOP  '''
# a = range (2,21,2)
# for i in a:
#     print(i)

# for i in range (2,21,2):
#     print(i)

# for i in range(21):
#     print(i)


# for i in range(1,21):
#     print(i)

# for i in range(20,0,-2):
#     print(i)

# for i in range(-15,-2):
#     print(i)

# for i in range(-5,-15,-1):
#     print(i)
  
# for i in range (5,51,5):
#     print(i)

# a = int(input("enter the number"))
# for i in range(a,a*10+1,a):
#     print(i)

# a = "sumit"
# for i in range(len(a)):
#     print(a[i])

# print(len(a))

# a = "sumit"
# for i in a:
#     print(i)

# for i in range(51):
#     if i == 15:
#         break
#     else:
#         print(i)

# for i in range(21):
#     if i==15:
#         continue
#     else:
#         print(i)

# for i in range(1,21):
#     if i == 12:
#         print("break executed")
#         break
#     print(i)
# else:
#     print("break not executed")

# for i in range(1,21):
#     if i == 12:
#         print("continue executed")
#         continue
#     print(i)
# else:
#     print("continue not executed")


# accept an intiger and print hello world n times
# n = int(input("enter the number"))
# for i in range(n):
#     print("hello World")

# # print natural number n times
# n = int(input("enter the number "))
# for i in range(1,n+1):
#     print(i)

# Reverse for loop print n to 1
# n = int(input("enter the number "))
# for i in range(n,0,-1):
#     print(i)

# take a number as input and print its table
# n = int(input("enter the number "))
# for i in range(n,n*10+1,n):
#     print(i*n)

# take a number as input and print its table
# n = int(input("enter the number "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}" )



# sum up to n terms
""" sum = 0
    sum = sum + 1
    sum = sum + 2   
    sum = sum + 3
    sum = sum + 4    """

# n = int(input("enter the number "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your sum in {sum}")

# facturial of a number.
# a = int(input("enter the number "))
# fact = 1
# for i in range(1,a+1):
#     fact *= i
#     print(fact)

# a = int(input("enter the number "))
# fact = 1
# for i in range(1,a+1):
#     fact = fact * i
#     print(fact)


# print the sum of even and odd numbers in a range separatly
# a = int(input("enter the number "))
# even_number = 0
# odd_number = 0
# for i in range(1,a+1):
#     if a%2 == 0:
#         even_number = even_number +i
#         print(even_number)
#         print("its a even number")
#     else:
#         odd_number = odd_number + i
#         print(odd_number)
#         print("its odd number")

"""   WRONG ANSWER ^  """

#  print the sum of even and odd numbers in a range separatly

# a = int(input("enter ther number"))
# for i in range(1,a+1):
#     if i%2 == 0:
#         print(i)

# a = int(input("enter ther number"))
# even = 0
# odd = 0
# for i in range (1,a+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd +i
# print(f"total num of even {even} and odd {odd}")


# Print all the facters of a number
# a = int(input("enter ther number"))
# factors = 0
# for i in range(1,a+1):
#     if a%i == 0:
#         print(i)

# Accept a number and check if it a perfect number of not
# a = int(input("enter ther number "))
# per = 0
# for i in range (1,a):
#     if a%i == 0:
#         per = per + i
# if per == a:
#     print(per)
#     print("its perfect number")
# else:
#     print("not a perfect number")


# a = int(input("enter ther number "))
# sum=0
# for i in range(1,a):
#     if a%i == 0:
#        sum = sum + i
# if sum == a:
#     print(f"{sum} is a perfect number")
# else:
#     print("Its not a perfect number")

# a = int(input("enter ther number "))
# b = 0
# for i in range(1,a):
#     if a%i == 0:
#         b = b + i
# if b == a:
#     b==a
#     print (f"{b} is perfect number")
# else:
#     print("not a pefect number")



# # check wether the number is prime or not
# a = int(input("check your number prime or not "))
# count = 0
# for i in range(1,a+1):
#     if a%i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")
# else:
#     print("not a prime number")


# reverse a string without using in build functions.
# a = "sumit"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# a = "sumit"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b +(a[i])
# print(b)


# check string is pallindrom or not?
# a = input("check string is pallindrom or not? ")
# b = ""
# for i in range (len(a)-1,-1,-1):
#     b = b + (a[i])
# if b == a:
#     print(f"{a} is a pallindrom")
# else:
#     print("NOT A PALLINDROM" )


# count all letters, digit and spacial symbols from a given string

a = "bjfas%5a64@dfa4dfa4f5!"
char = 0
digit = 0
spatial = 0
for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char += 1
    else:
        spatial+=1
print(f"your digits are {digit}\nyour char are {char}\nyour spatial are{spatial}")