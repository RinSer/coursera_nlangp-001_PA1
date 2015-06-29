
# Tagger based on Viterbi algorithm:

fileDev = open('C:\Python2\gene.test', 'r')
fileE = open('C:\Python2\emissionR.parameters', 'r')
fileQ = open('C:\Python2\ml.parameters', 'r')

# Input:

# Define tags:

tags = ('O', 'I-GENE') # states

# Define sentences:
sentences = []
sentence = []  # observations
line = fileDev.readline()
while line != '':
    if line != '\n':
        sentence.append(line[:-1])
    else:
        sentences.append(sentence)
        sentence = []  
    line = fileDev.readline()

fileDev.close()

# Define probability of the first word containing each tag:

start_probability = {'* O' : 0.945708901131, '* I-GENE' : 0.0542910988692}

# Define parameters:
mls = fileQ.readlines()
mlD = {}  # transition probability
for ml in mls:
    mlD.setdefault(str(ml.split(' ')[0]), {})[str(ml.split(' ')[2]) + ' ' + str(ml.split(' ')[4])] = float(ml.split(' ')[5][:-1])

ems = fileE.readlines()
emD = {}  # emission probability
for em in ems:
    emD.setdefault(str(em.split(' ')[0]), {})[str(em.split(' ')[1])] = float(em.split(' ')[2][:-1])


# The algorithm function:

def viterbi(sentence, tags, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base case (n == 0)
    for y in tags:
        if sentence[0] in emit_p:
            if y in emit_p[sentence[0]]:
                V[0]['* ' + y] = start_p['* ' + y] * emit_p[sentence[0]][y]
                path[y] = [y]
            else:
                V[0]['* ' + y] = 0
                path[y] = [y]
        else:
            V[0]['* ' + y] = start_p['* ' + y] * emit_p['_RARE_'][y]
            path[y] = [y]
       
    # Run VA for n > 0:
    for n in range(1, len(sentence)):
        V.append({})
        newpath = {}

        for y in tags:
            if sentence[n] in emit_p:
                if y in emit_p[sentence[n]]:
                    if n == 1:
                        for y0 in tags:
                            (prob, tag) = max((V[0]['* ' + path[y0][0]] * trans_p[y]['* ' + path[y0][0]] * emit_p[sentence[n]][y], y0) for y0 in tags)
                            V[1][path[tag][0] + ' ' + y] = prob
                            newpath[y] = path[tag] + [y]
                    else:
                        (prob, tag) = max((V[n-1][str(path[y0][n-2]) + ' ' + str(path[y0][n-1])] * trans_p[y][str(path[y0][n-2]) + ' ' + str(path[y0][n-1])] * emit_p[sentence[n]][y], y0) for y0 in path)
                        V[n][path[tag][n-1] + ' ' + y] = prob
                        newpath[y] = path[tag] + [y]
            else:
                if n == 1:
                    (prob, tag) = max((V[0]['* ' + path[y0][0]] * trans_p[y]['* ' + path[y0][0]] * emit_p['_RARE_'][y], y0) for y0 in tags)
                    V[1][path[tag][0] + ' ' + y] = prob
                    newpath[y] = path[tag] + [y]
                else:
                    (prob, tag) = max((V[n-1][str(path[y0][n-2]) + ' ' + str(path[y0][n-1])] * trans_p[y][str(path[y0][n-2]) + ' ' + str(path[y0][n-1])] * emit_p['_RARE_'][y], y0) for y0 in path)
                    V[n][path[tag][n-1] + ' ' + y] = prob
                    newpath[y] = path[tag] + [y]
            

        # Do not need to remember the old paths
        path = newpath
    w = 0   # if only one word is observed, max is sought in the initialization values
    if len(sentence) == 1:
        (prob, tag) = max((V[0]['* ' + path[y][0]] * trans_p['STOP']['* ' + y], y) for y in tags)
    else:
        w = n
    # print_stable(V)
    (prob, tag) = max((V[w][str(path[y][w-1]) + ' ' + str(path[y][w])] * trans_p['STOP'][str(path[y][w-1]) + ' ' + str(path[y][w])], y) for y in path)
    # return (prob, path[tag])
    return path[tag]

    
# Function that prints a table of steps:
def print_stable(V):
    s = "   " + " ".join(("%.7s" % i) for i in range(len(V))) + '\n'
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += '\n'
    print(s)

# Execute:

# observations = sentences[3]
states = tags
transition_probability = mlD
emission_probability = emD
        
    # Function to execute viterbi:
def execute():
    fileOT = open('C:\Python2\gene_test.p2.out', 'w')
    
    i = 0
    Tags = []
    while i < len(sentences):
        observations = sentences[i]
        Tags.append(viterbi(observations,
                       states,
                       start_probability,
                       transition_probability,
                       emission_probability))
        i = i + 1

    for m in range(len(sentences)):
        for n in range(1, (len(sentences[m]) + 2)):
            if n <= len(sentences[m]):
                fileOT.write(sentences[m][n - 1] + ' ' + str(Tags[m][n - 1]) + '\n')
            elif n == (len(sentences[m]) + 1):
                fileOT.write('\n')

    fileOT.close()

    # return Tags
    return 'Mission complete'



