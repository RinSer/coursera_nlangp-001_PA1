
# Tagger based on Viterbi algorithm:

fileDev = open('C:\Python2\genet.dev', 'r')
fileE = open('C:\Python2\emissionRt.parameters', 'r')
fileQ = open('C:\Python2\ml.parameters', 'r')
'''
# Algorithm to find sentences in data:
sentences = []
line = fileDev.readline()
sentence = ''
while line != '':
    if line != '\n':
        if line != '.\n':
            sentence = sentence + line[:-1] + ' '
        else:
            sentence = sentence + line
            sentences.append(sentence)
            sentence = ''
    line = fileDev.readline()
'''
# Input:

# Define tags:

tags = ('O', 'I-GENE') # states
start_tags = ('*', 'O', 'I-GENE')

# Define sentences:
sentences = []
sentence = []  # observations
line = fileDev.readline()
while line != '':
    if line != '\n':
        if line != '.\n':
            sentence.append(line[:-1])
        elif line == '.\n':
            sentence.append(line[:-1])
            sentences.append(sentence)
            sentence = []  
    line = fileDev.readline()
'''    else:
        sentences.append('\n')'''
fileDev.close()

# Define probability of the first word containing each tag:

start_probability = {'O' : 0.945708901131, 'I-GENE' : 0.0542910988692}

# Define parameters:
mls = fileQ.readlines()
mlD = {}  # transition probability
for ml in mls:
    mlD.setdefault(str(ml.split(' ')[0]), {})[str(ml.split(' ')[4])] = float(ml.split(' ')[5][:-1])



ems = fileE.readlines()
emD = {}  # emission probability
for em in ems:
    emD.setdefault(str(em.split(' ')[1]), {})[str(em.split(' ')[0])] = float(em.split(' ')[2][:-1])

# The algorithm function:

def viterbi(sentence, tags, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base case (n == 0)
    for y in tags:
        if sentence[0] in emit_p[y]:
            V[0][y] = start_p[y] * emit_p[y][sentence[0]]
            path[y] = [y]
        else:
            V[0][y] = start_p[y] * emit_p[y]['_RARE_']
            path[y] = [y]
        

    # Run VA for n > 0:
    for n in range(1, len(sentence)):
        V.append({})
        newpath = {}

        for y in tags:
            if sentence[n] in emit_p[y]:
                (prob, tag) = max((V[n-1][y0] * trans_p[y0][y] * emit_p[y][sentence[n]], y0) for y0 in tags)
                V[n][y] = prob
                newpath[y] = path[tag] + [y]
            else:
                (prob, tag) = max((V[n-1][y0] * trans_p[y0][y] * emit_p[y]['_RARE_'], y0) for y0 in tags)
                V[n][y] = prob
                newpath[y] = path[tag] + [y]
            

        # Do not need to remember the old paths
        path = newpath
    w = 0   # if only one word is observed, max is sought in the initialization values
    if len(sentence) != 1:
        w = n
    print_stable(V)
    (prob, tag) = max((V[w][y] * trans_p['STOP'][y], y) for y in tags)
    return (prob, path[tag])

# Function that prints a table of steps:
def print_stable(V):
    s = "   " + " ".join(("%.7s" % i) for i in range(len(V))) + '\n'
    for y in V[0]:
        print y
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += '\n'
    print(s)

# Example:

observations = sentences[0]
states = tags
transition_probability = mlD
emission_probability = emD
        
        
def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)



