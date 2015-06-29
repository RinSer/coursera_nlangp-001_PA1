# Map rare words from training data to 4 classes

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
        if (listL.count(listL[i].split(' ')[0] + ' O\n') + listL.count(listL[i].split(' ')[0] + ' I-GENE\n')) < 5:
            if listL[i] != '\n':
                if listL[i].split(' ')[0].isalnum() and not listL[i].split(' ')[0].isalpha():
                    listL[i] = '_NUM_ ' + ' ' + listL[i].split(' ')[1]
                elif listL[i].split(' ')[0].isupper() and listL[i].split(' ')[0].isalpha():
                    listL[i] = '_CAP_ ' + ' ' + listL[i].split(' ')[1]
                elif not listL[i].split(' ')[0][:-1].isupper() and listL[i].split(' ')[0][-1].isupper():
                    listL[i] = '_LCAP_ ' + ' ' + listL[i].split(' ')[1]
                else:
                    listL[i] = '_RARE_ ' + ' ' + listL[i].split(' ')[1]


new_file = open('C:\Python2\geneR4.train', 'w')

for item in listL:
    new_file.write(item)

new_file.close()

print 'Mission complete'
               
