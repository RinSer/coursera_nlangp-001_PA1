# Map rare words from training data to a common symbol _RARE_

'''fileGT = open('C:\Python2\genet.train', 'r')

textL = []
line = fileGT.readline()
while line != '':
    word = line.split(' ')[0]
    if word != '\n':
        textL.append(word)
    line = fileGT.readline()


for i in range(len(textL)):
    if textL.count(textL[i]) < 5:
        textL[i] = '_RARE_'
'''
'''wordDict = {}
with open('C:\Python2\genet.train') as fileGT:
    listL = fileGT.readlines()
    for i in range(len(listL)):
        if listL[i] != '\n':
            wordDict[listL[i].split(' ')[0]] = listL[i].split(' ')[1]

with open('C:\Python2\genet.train') as fileGT:
    listL = fileGT.readlines()
    for i in range(len(listL)):'''
        

        

with open('C:\Python2\gene.train') as fileGT:
    listL = fileGT.readlines()
    for i in range(len(listL)):
        '''if listL[i] != '\n':
            print listL.count(listL[i].split(' ')[0] + ' O\n') + listL.count(listL[i].split(' ')[0] + ' I-GENE\n')
        else:
            print listL.count('\n')'''
        if (listL.count(listL[i].split(' ')[0] + ' O\n') + listL.count(listL[i].split(' ')[0] + ' I-GENE\n')) < 5:
            if listL[i] != '\n':
                listL[i] = '_RARE_ ' + ' ' + listL[i].split(' ')[1]

new_file = open('C:\Python2\geneR.train', 'w')

for item in listL:
    new_file.write(item)

new_file.close()

print 'Mission complete'
               
