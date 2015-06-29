fileI = open('C:\Python2\geneRC.counts', 'r')


line = fileI.readline()
# Total counts of tags O and I-GENE
countO = 0
countG = 0
while line != '41072 1-GRAM I-GENE\n':
    arg = line.split()
    if arg[2] == 'O':
        countO = countO + int(arg[0])
    else:
        countG = countG + int(arg[0])
    line = fileI.readline()
cO = float(countO)
cG = float(countG)

fileI.close()

# Count emission parameters for each word: e(X|Y) = Count(Y->X)/Count(Y)
fileI = open('C:\Python2\geneRC.counts', 'r')
fileW = open('C:\Python2\emissionRC.parameters', 'w')

line = fileI.readline()
while line != '41072 1-GRAM I-GENE\n':
    arg = line.split()
    if arg[2] == 'O':
        e = float(arg[0]) / cO
        new_line = [arg[3], arg[2], e]
    else:
        e = float(arg[0]) / cG
        new_line = [arg[3], arg[2], e]
    fileW.write(new_line[0] + ' ' + new_line[1] + ' ' + str(new_line[2]) + '\n')
    line = fileI.readline()

fileI.close()
fileW.close()
print 'mission complete'


    
