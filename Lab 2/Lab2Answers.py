# # 10. Write a program that reads in 10 strings from the keyboard. 
# # Count the number of strings that start with 'pr'. Display this count. Use a loop.

# i=0
# pr = 0
# while i <10:
#     x = input("enter a string: ")
#     i+=1
#     if 'pr' in x:
#         pr += 1
# print(pr)

# # 11. Write a program that reads in a positive integer into n. 
# # Your program should then display True if n is a perfect number, and False 
# # otherwise A perfect number is a number whose positive divisors excluding itself sum up to the given number. 
# # For example, the positive divisors of 6 excluding 6 are 1, 2, and 3. Because 1 + 2 + 3 = 6, 6 is a perfect number.

# num = int(input('enter a number: '))
# i = 1
# sum = 0
# if num > 0:
#     while (i < num):
#         if num % i == 0:
#             sum = sum + i
#         i += 1
#     if sum == num:
#         print("true")
#     else:
#         print("false")


# # 12. Write a program that reads in a text file that consists of some standard English text. 
# # Your program should count the number of occurrences of each letter of the alphabet, 
# # and display each letter with its count, in the order of increasing count. 
# # What are the six most frequently used letters?

# infile = open('lab2.txt', 'r')
# source = infile.read()
# d={}
# for char in set(source):
#     if char.isalpha():        
#         d[char]=source.count(char)
# sorted_d = sorted(d.items(), key = lambda kv: kv[1])
# print('\nLetter count' + str(sorted_d))

# x = 6
# most_freq = sorted_d[-x:]
# print('\nthe most frequent letters are: ' + str(most_freq))


# # 13. Write a program that reads in a string and determines if it is a palindrome (
# #     i.e., a string that reads the same backwards as forwards).

# def isPal(word):
#     return word == word[::-1]

# word = str(input("enter a word: "))
# if isPal(word):
#     print('yes!')
# else:
#     print('no')

        
# 14. Write a program that computes the following sum: 2 + 1/2! + 1/3! + ⋯ + 1/100! 
# Is the sum equal to an important constant in mathematics? “!” denotes the factorial function. 
# n! is the product of the integers from 1 to n. For example, 5! = 1×2×3×4×5 = 120.

import math
n=2
sum = 2
while n<=100:
    sum = sum + (1/math.factorial(int(n)))
    n+=1
print("sum = " + str(sum))


# TODO: 15. Write a program that reads in 10 numbers, placing each one on a linked list. 
# Your program should then display each number by traversing the linked list using a loop and using recursion.

class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

def newNode(new_data):
   new_node = Node(new_data)
   new_node.data = new_data
   new_node.next = None
   return new_node

def insertEnd(head, new_data):
    if (head == None):
        return newNode(new_data)
    else:
       head.next = insertEnd(head.next, new_data)
    return head

def traverserec(head):
   if (head == None):
       return
   print(head.data, '->', end = " ")
   traverserec(head.next)

def traverseloop(head):
   while(head != None):
       print(head.data, '->', end = " ")
       head = head.next
   return
  
if __name__=='__main__':
   head = None
   i=1
   while(i<=10):
       head = insertEnd(head, int(input("Enter a number: ")))
       i+=1
   traverserec(head)
   print()
   traverseloop(head)



# 16. Write a program that reads in a positive integer into n. Your program should then sum up the first n positive odd numbers, 
# and display the sum. What is the relation between the value of n and the computed sum?

# def oddSum(n) :
#     sum = 0
#     curr = 1
#     i = 0
#     while i < n:
#         sum = sum + curr
#         curr = curr + 2
#         i = i + 1
#     return sum
# n = int(input('enter a number: '))
# print (oddSum(n) )
# print('The computed sum is equal to n^2')





# 17. Read in a positive number into x. Then execute the following statement 
# 100 times: x = math.sqrt(x)
# Does the value of x converge on a particular number, regardless of its initial value? 
# Try values both less than and greater than 1. To use sqrt(), import the math module.
# import math
# x = float(input("enter a positive number: "))
# if x<0:
#     print('number must be positive')
# else:
#     i = 1
#     while i <= 100:
#         x = math.sqrt(x)
#         i += 1
#     print(x)



# 18. Write a program that reads in a positive integer into n. Your program should then display n rows. 
# Each row should have consecutive integers starting from 1, and have one more integer than the preceding row. 
# The first row should should contain only 1. For example, if 3 is entered, then your program should display
# 1
# 1 2 
# 1 2 3

# num = int(input("enter a number: "))
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')