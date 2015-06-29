# Function to compute Trigram ML Parameters for training data:

fileTR = open('C:\Python2\geneR_tr.counts', 'r')
filePR = open('C:\Python2\ml.parameters', 'w')

counts = fileTR.readlines()

for i in range(len(counts)):
    for j in range(len(counts)):
        if counts[i].split(' ')[1] == '2-GRAM' and counts[j].split(' ')[1] == '3-GRAM':
            if counts[i].split(' ')[2] == counts[j].split(' ')[2] and counts[i].split(' ')[3][:-1] == counts[j].split(' ')[3]:
                par = counts[j].split(' ')[4][:-1] + ' | ' + counts[j].split(' ')[2] + ' , ' + counts[j].split(' ')[3] + ' '
                val = float(counts[j].split(' ')[0]) / float(counts[i].split(' ')[0])
                ent = par + str(val) + '\n'
                filePR.write(ent)
            

fileTR.close()
filePR.close()

print 'Mission complete'


    

