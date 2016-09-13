from functools import reduce
from random import uniform, choice

class MarkovChain:
    def __init__(self, iterations):
        self.iterations = iterations

    def initMTuple(self, path):
        TDict = {}
        Tokens = []
        with open(path, 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    Tokens.append(word)
                    if word != [] and word not in TDict.keys():
                        TDict[word] = []
        return TDict, Tokens

    def initSimpleChain(self, Tokens, TDict):
        for i,word in enumerate(Tokens):
            if i != len(Tokens) -1:
                sym = Tokens[i + 1]
            if [sym] not in [list(x.keys()) for x in TDict[word]]:
                TDict[word].append(dict({sym:1}))
            else:
                for d in TDict[word]:
                    if d.get(sym):
                        d[sym] += 1

    def buildProbabilities(self, TDict):
        for key in TDict:
            Sum = [list(d.values()) for d in TDict[key]]
            for d in TDict[key]:
                for key in d:
                    d[key] = d[key] / reduce(lambda x, y: x + y, reduce(lambda x,y: x+y, Sum))

    def buildText(self, Chain):
        self.state = outText = choice(list(Chain.keys()))
        for i in range(self.iterations):
            step = uniform(0, 1)
            self.getState(Chain)
            outText = outText + ' ' + self.state + ' '
        return outText

    def getState(self, Chain):
        step = uniform(0, 1.1)
        print('Current step is: ', step, ' And state is: ', self.state)
        for d in Chain[self.state]:
            self.state = choice(list(d.keys()))
            return