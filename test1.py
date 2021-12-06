# Array in accending order
# car = [1,3,4,2,5,8,1]
# print(car)
# for i in range(len(car)):
#     for j in range(i+1,len(car)):
#         if car[i]>car[j]:
#             temp = car[i]
#             car[i]= car[j]
#             car[j]= temp
# print(car)
#swappig the two number
# a=2
# b=7
# print(a,b)
# a= a+b
# b=a-b
# a=a-b
# print(a,b)
# Python Program to Print the Fibonacci sequence
# nterm=int(input(print("Enter the nth term")))
# a=0
# b=1
# if nterm<0:
#     print("please enter the positve integer")
# elif nterm==0:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(nterm-2):
#         c=a+b
#         a=b
#         b=c
#         print(c)

# Prime Numbers
# num=int(input(print("enter the number")))
# if (num==1) or (num == 0):
#     print("not prime number")
# else:
#     count=0
#     for i in range(2,num+1):
#         if num%i==0:
#             count+=1
#     if count==1:
#         print("prime number")
#     else:
#         print("not prime numbers")

# prime number between 1 to 100
# num=1000
# for i in range(1,num+1):
#     count=0
#     for j in range(2,i+1):
#         if i%j==0:
#             count+=1
#     if count==1 or i%13==0:
#         print(i, end=" ")

# factorail
# num = int(input(print("enter the number")))
# fact =1
# for i in range(num,0,-1):
#     fact=fact*i
# print(fact)
# prefect number between 1 to 100
# num = 100
# for i in range(1,num+1):
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             sum=sum+j
#     # print("sum of ",i,sum)
#     if i==sum:
#         print(i)

# Reverse the string
# def reverse(text):
#     # return text[::-1]
#     rev = ""
#     for i in text:
#         rev = i+rev
#     return rev
# print(reverse("shiv"))

# Program to determine whether a given string is Palindrome

# def Palindrome(text):
#     # return text[::-1]
#     text=text.lower()
#     rev = ""
#     for i in text:
#         rev = i+rev
#     if rev == text:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
# Palindrome("Kayak")

# fins the matching character
# str1="loveyou"
# str2="abceyco"
# s1= set(str1)
# s2=set(str2)
# common = s1 & s2
# print( "Matching character are ",common)
# text = input(print("Enter the word"))
# text=text.lower()
# vol=0
# cons=0
# for i in text:
#     if (i=="o" or i=='a' or i=='e' or i=='i' or i=='u'):
#         vol+=1
#     else:
#         cons+=1
# print("number of vol ",vol)
# print("number of cons ", cons)
# Python Program to Check if Two Strings are Anagram

# s1='listen'
# s2='silent'
# if (sorted(s1)==sorted(s2)):
#     print("Strings are Anagram")
# else:
#     print("Strings are not Anagram")
            
# rotation of strings
# s1="abcde"
# s2="deabc"
# if(len(s1)!= len(s2)):
#     print("Second string is not a rotation of first string")
# else:
#     s3=s1+s2
#     if(s3.index(s2)):
#         print("Second string is a rotation of first string")
#     else:
#         print("Second string is not a rotation of first string")

# calculate the numbric value of digits
# s1 = "wdsdcsdfexsd1d2"
# num1=['0','1','2']
# alp=['a','b','c','d']
# char1=0
# num=0
# for i in s1:
#     if i in num1:
#         num+=1
#     elif i in alp:
#         char1+=1
# print(num,char1)

# num = int(input(print("Enter the number")))
# sum=0
# for i in str(num):
#     sum=sum+int(i)
# print(sum)
# num =123
# sum=0
# while num!=0:
#     sum=sum+(num%10)
#     num=num//10
# print(sum)
# missing number from the natural number 
# num =[1,2,3,4,5,6,8,9]
# length = len(num)
# sum_of_num=0
# total = (length+1)*(length+2)/2
# sum_of_num =sum(num)
# missing_digit=total-sum_of_num
# print(missing_digit)
# largest number

arr =[1,3,4,5,2,5,90,43,100,55,33,-2, 99]
# maxm=arr[0]
# minm=arr[0]
# second_large=arr[0]
# for j in range(len(arr)):
#     if maxm<arr[j]:
#         maxm=arr[j]
#     elif minm>arr[j]:
#         minm=arr[j]
# for j in range(len(arr)):
#     if second_large<arr[j] and arr[j]<maxm:
#         second_large=arr[j]
# print(maxm,minm,second_large)
print(arr)
arr = arr[::-1]
print(arr)
