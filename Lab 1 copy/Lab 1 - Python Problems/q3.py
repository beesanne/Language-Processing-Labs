import sys
# infile = open(sys.argv[1], 'r')
# source = infile.read()
# outfile = open(sys.argv[2], 'w')
# with open(sys.argv[2]) as outf:
#     for i, line in enumerate(outf):
#         sys.stdout.write('%04d %s'%(i, line))

# # with open(sys.argv[2] for f1):
# #     if line 
# # outfile.write("1 %4d" + source)
# outfile.close()



# import sys
# infile = open(sys.argv[1], 'r')
# source = infile.read()
# outfile = open(sys.argv[2], 'w')
# outfile.write(source)
# outfile.close()

# import sys
# infile = open(sys.argv[1], 'r')
# source = infile.read()
# outfile = open(sys.argv[2], 'w')
# outfile.write(source)
# outfile.close()



with open(sys.argv[1], 'r') as program:
    data = program.readlines()

with open(sys.argv[2], 'w') as program:
    for (number, line) in enumerate(data):
        program.write('%d %4s %s' % (number + 1, ' ', line))
