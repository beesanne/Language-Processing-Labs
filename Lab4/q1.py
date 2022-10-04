
import sys   # needed to access command line arg

#global variables
tokenindex = -1
token = ''


def main():
   try:
      parser()         # call the parser
   except RuntimeError as emsg:
      print(emsg)


def advance():
   global tokenindex, token
   tokenindex += 1     # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      token = ''      # signal the end by returning null string
   else:
      token = sys.argv[1][tokenindex]


def consume(expected):
   if expected == token:
      advance()
   else:
      raise RuntimeError('Expecting ' + expected)


def parser():
   advance()   # prime token with first character
   S()         # call function for start symbol
   # test if end of input string
   if token != '':
      print('Garbage following <S>-string')

# Q1

# Grammar:
# S -> aSb
# S -> c

# S->aSb->aaSbb->aaaSbbb->aaacbbb
# def S():
#     if token == 'a':
#         advance()
#         S()
#         consume('b')
#     elif token == 'c':
#         advance()
#     else:
#         raise RuntimeError('expecting a or c')

# Q2
# Grammar 
# S -> aBd
# B -> (bb)*[c]

# def S():
#     if token == 'a':
#         advance()
#         B()
#         consume('d')
#     elif token == 'd':
#         advance()
#     else:
#         raise RuntimeError ('expecting a')

# def B():
#     while token == 'b':
#         advance()
#         consume('b')
#     if token == 'c':
#         advance()

# Q3
# Grammar:
# S -> a*B
# B -> b*C
# C -> c[d|e]f

def S():
    while token =='a':
        advance()
    B()

def B():
    while token =='b':
        advance()
    C()

def C():
    consume('c')
    if token == 'd':
        advance()
    elif token == 'e':
        advance()
    consume('f')

main()
