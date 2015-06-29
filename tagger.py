# Baseline tagger program.
'''file('emission parameters: (word tag e) each line', 'r'),
file('word to be tagged each line', 'r') -> file('(word tag) each line, 'w')

Returns file with words recieving tag, which emission parameter for particular
word is greater.

'''
'''
fileTR = open('C:\Python2\emissionR.parameters', 'r')

tList = fileTR.readlines()

# Find max emission parameter for each word and store it in a dictionary:

# Find max emission parameters if exist two of them:
tagDict = {}
for i in range(len(tList)):
    for j in range(len(tList)):
        if tList[i].split(' ')[0] == tList[j].split(' ')[0] and tList[i].split(' ')[1] != tList[j].split(' ')[1]:
            if float(tList[i].split(' ')[2]) > float(tList[j].split(' ')[2]):
                tagDict[tList[i].split(' ')[0]] = tList[i].split(' ')[1]
            else:
                tagDict[tList[j].split(' ')[0]] = tList[j].split(' ')[1]

# Find all single emission parameters:
for k in range(len(tList)):
    if not (tList[k].split(' ')[0] in tagDict):
        tagDict[tList[k].split(' ')[0]] = tList[k].split(' ')[1]

# Write dictionary into a file:

fileD = open('C:\Python2\maxemR.tags', 'w')

for key in tagDict:
    fileD.write(key + ' ' + tagDict[key] + '\n')

print 'mission complete'''
# Add dictionary tag values to words from file:

fileW = open('C:\Python2\gene.test', 'r') # file with words to be tagged
fileD = open('C:\Python2\maxemR.tags', 'r') # file with tag dictionary
fileT = open('C:\Python2\gene_test.p1.out', 'w') # output file

dictionary = fileD.readlines()
tagDict = {}
for line in dictionary:
    tagDict[line.split(' ')[0]] = line.split(' ')[1]

fileD.close()   

word = fileW.readline()
while word != '':
    if word[:-1] in tagDict:
        fileT.write(word[:-1] + ' ' + tagDict[word[:-1]])
    elif word == '\n':
        fileT.write('\n')
    else:
        fileT.write(word[:-1] + ' ' + tagDict['_RARE_'])
    word = fileW.readline()

fileW.close()
fileT.close()

print 'mission complete'



                
            
        
                
                            
                               
                                    
