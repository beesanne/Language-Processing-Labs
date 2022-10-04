# #1. PRINT NAME 10 TIMES USING A LOOP 
# print('\nQuestion1: ')
# n = 1
# while n <= 10:
#     print('Beesanne')
#     n+=1


# #2. READ IN A TEXTFILE AND OUTPUT THE EXACT COPY TO ANOTHER FILE 
# print('\nQuestion2:')
# import sys
# infile = open(sys.argv[1], 'r')
# source = infile.read()
# outfile = open(sys.argv[2], 'w')
# outfile.write(source)
# outfile.close()

# #3. SAME AS 2, BUT OUTPUT FILE SHOULD BE PREFIX WITH ITS LINE NUMBER OCCUPYING 4 SPACES
# print('\nQuestion3:')
# with open(sys.argv[1], 'r') as program:
#     data = program.readlines()

# with open(sys.argv[2], 'w') as program:
#     for (number, line) in enumerate(data):
#         program.write('%d %4s %s' % (number + 1, ' ', line))

# #4. WRITE A PROGRAM THAT DOES A LOOP THAT PROMPTS THE USER FOR A NUMBER, SQUARES IT, AND DISPLAYS THE ANSWER, EXIT WHEN 0
# print('\nQuestion4: ')
# x=input('enter a number: ')
# num = 0
# while x != 0:
#     num = int(x) ** 2
#     print(num)
#     x=int(input('enter a number: '))

    
# #5  Reads 10 integers, append to list, then display the list from beginning to end using a loop
# #   then display from end to beginning accessing with negative index, then with pop()
# print('\nQuestion5: ')
# list = []
# i=0
# while i < 10:
#     x = int(input('Enter an number: '))
#     list.append(x)
#     i+=1
# print('\nlist from beggining to end: ' )
# j=0
# while j < 10:
#     print(list[j])
#     j+=1
    
# print('\nlist from end to beggining with index: ')
# w= 1 
# while w <= 10:
#     print(list[w*-1])
#     w+= 1
# print('\nlist from end to beggining with pop: ')
# p=1 
# while p<=10:
#     print(list.pop())
#     p+=1
    


# #6 a function that is passed two lists, concat the 2nd to the 1st and return the new 1st 
# print('\nQuestion6: ')
# def concat(l1, l2):
#     for i in l2:
#         l1.append(i)
#     return l1

# test_l1 = [1, 2, 3]
# test_l2 = [4, 5, 6,]
# print(concat(test_l1, test_l2))


# #7 read a string and display its length 
# print('\nQuestion7: ')
# x = str(input('enter a string: '))
# print(len(x))


# #8 Call function getgrade() repeatidly until it returns a valid grade. 
# #  prompt user to enter an int 0-100 
# #  raise a runtimeError indicating invalid grade 
# #  when valid it should display what quartile its in. 

# print('\nQuestion8: ')
# def getgrade(grade):
#     if grade>=0 and grade <= 100:
#         if grade<=24 and grade>=0:
#             print('4th quatile')
#         elif grade>=25 and grade<=49:
#             print('3rd quartile')
#         elif grade>=50 and grade<=74:
#             print('2nd quartile')
#         elif grade>=75 and grade<=100:
#             print('1st quartile')
#     else:
#         raise RuntimeError("Not valid grade")
# try:
#     getgrade(int(input('Enter Grade: ')))
# except RuntimeError as emsg:
#     print(emsg)


# #9 creates a dictionary whos keyvalue pairs are a/1 b/2...z/26
# #  then prompt for and read a letter and display its value 
print('\nQuestion9: ')
from string import ascii_lowercase as letternum
dict={}
num = 1
for i in letternum:
    dict[i] = num
    num+=1

x = input('Enter a Letter: ')
print(dict[x])